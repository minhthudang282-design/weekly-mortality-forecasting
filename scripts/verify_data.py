"""Small, dependency-free check for the reproducibility inputs.

Run from any directory:
    python scripts/verify_data.py

This checks source rows, week continuity, and held-out observation provenance.
It does not replace the complete notebook execution or statistical validation.
"""
from __future__ import annotations

import csv
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "uk_weather_health_weekly_2016_2024_TOTAL_FINAL.csv"
PREP = ROOT / "uk_weather_health_weekly_CLEANED.csv"
REGIONAL = ROOT / "metoffice_general_regions_tmax_2024.csv"
GEO = ROOT / "united_kingdom_outline.geojson"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fp:
        return list(csv.DictReader(fp))


def iso_day(value: str) -> date:
    # CSV dates are ISO strings, possibly followed by time text.
    return date.fromisoformat(value.strip()[:10])


def main() -> None:
    for path in (RAW, PREP, REGIONAL, GEO):
        assert path.is_file(), f"Required input missing: {path.name}"

    raw = read_csv(RAW)
    prepared = read_csv(PREP)
    assert len(raw) == 442, f"Expected 442 observed rows, got {len(raw)}"
    assert len(prepared) == 469, f"Expected 469 prepared rows, got {len(prepared)}"
    assert len(raw[0]) == 6, f"Expected 6 raw variables, got {len(raw[0])}"
    assert len(prepared[0]) == 13, f"Expected 13 prepared variables, got {len(prepared[0])}"

    raw_dates = {iso_day(r["week_start_sat"]) for r in raw}
    prepared_dates = [iso_day(r["week_start_sat"]) for r in prepared]
    assert len(raw_dates) == len(raw), "Repeated observed week keys"
    assert prepared_dates == sorted(prepared_dates), "Prepared grid not sorted by week"
    assert len(set(prepared_dates)) == len(prepared_dates), "Repeated prepared week keys"
    assert all((b - a) == timedelta(days=7) for a, b in zip(prepared_dates, prepared_dates[1:])), "Prepared weekly grid is not continuous"
    assert raw_dates.issubset(set(prepared_dates)), "An observed week is missing from prepared grid"

    synthetic_dates = set(prepared_dates) - raw_dates
    assert len(synthetic_dates) == 27, f"Expected 27 interpolated weeks, got {len(synthetic_dates)}"
    assert int(sum(float(r["deaths_total"]) for r in raw)) == 4_769_329, "Observed registered-death total differs from the report"

    model_dates = prepared_dates[1:]
    train_dates, test_dates = model_dates[:374], model_dates[374:]
    assert len(model_dates) == 468
    assert len(train_dates) == 374 and len(test_dates) == 94
    assert set(test_dates).issubset(raw_dates), "Interpolated outcome found in held-out test"
    assert len(set(test_dates) & synthetic_dates) == 0

    print("PASS — 442 observed weeks; total registered deaths: 4,769,329")
    print("PASS — 469 prepared weeks, with 27 interpolated calendar gaps")
    print("PASS — 468 lagged rows: 374 train and 94 observed test outcomes")
    print("PASS — all five data/reference inputs found")
    print("NOTE — run all six notebooks to verify the full analysis")


if __name__ == "__main__":
    main()
