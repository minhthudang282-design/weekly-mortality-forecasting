# Weekly Mortality Forecasting — corrected notebooks

## Running the project

1. Keep **all six notebooks and five data/reference files in this folder**, unchanged filenames.
2. Install dependencies from `requirements.txt` in a Python 3.11+ environment.
3. Open Jupyter in this folder and choose **Kernel -> Restart Kernel and Run All Cells** for notebooks **1 through 6, in numerical order**.
4. Notebook 2 writes `uk_weather_health_weekly_CLEANED.csv`; the provided copy is a reference. Notebooks 3–5 describe 442 observed weeks. Notebook 5 uses the 469-week grid for seasonal decomposition only; Notebook 6 uses 468 lagged rows and a chronological 374/94 split.
5. Inspect the final `Final checks / Verification` cell in each notebook; see `RUN_ALL_VALIDATION.txt` for the locally tested execution record.

## Inputs
- `uk_weather_health_weekly_2016_2024_TOTAL_FINAL.csv`: 442 observed registrations weeks (not separate source raw ONS and Met Office files).
- `uk_weather_health_weekly_CLEANED.csv`: 469 regular-week observations + interpolated values; interpolated rows must not be counted as real registrations.
- `uk_weather_health_data_dictionary.csv`: description and units of fields.
- `metoffice_general_regions_tmax_2024.csv`: separate 2024 regional temperatures.
- `united_kingdom_outline.geojson`: geometry for the regional-temperature figure.

## Evidence limits
- Registered deaths in England & Wales and mean weekly UK-wide Tmax have different spatial scope.
- The strongest simple lag correlation does not establish causality.
- Retrospective forecast models with observed temperature in the target week are not real-time weather-warning systems.
- The published fixed-alpha model comparison reused a holdout in model selection. The rebuilt exploratory Ridge/Lasso selection uses training-only time-series cross-validation, and paper-matched metrics are separately retained with their original limitation.

## Shapely note (Notebook 5)
Notebook 5 Figure 5 requires Shapely to clip the UK map geometry. Install the full requirements before Run All (`python -m pip install -r requirements.txt`) or run `%pip install shapely` inside the Jupyter kernel. The Figure 5 cell now attempts a one-time installation into the active kernel only when Shapely is missing. The map code, figures, and paper-aligned results are unchanged. If pip has no internet access, install Shapely before starting the notebook.
