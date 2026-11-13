# Troubleshooting notebook execution

## `ModuleNotFoundError: No module named 'shapely'` (Notebook 5)

Install requirements into the active Jupyter environment:

```python
%pip install -r requirements.txt
```

Alternatively, for the geometry dependency only:

```python
%pip install shapely
```

Then select **Kernel → Restart Kernel and Run All Cells**. A package installed into a different Python environment will not automatically be available in your notebook's kernel.

## `FileNotFoundError` when loading CSV or GeoJSON

Open Jupyter from the repository root, where the six notebooks and the five CSV/GeoJSON inputs are kept together. For example:

```bash
cd weekly-mortality-forecasting
jupyter lab
```

Do not move the notebooks or data into different folders without updating their relative paths.

## Notebook 2 regenerates the prepared CSV

This is expected: Notebook 2 writes `uk_weather_health_weekly_CLEANED.csv` from the observed input. The repaired code was checked to reproduce the distributed prepared file. Do not interpret the interpolated 27 calendar weeks as additional observed mortality registrations.

## Why can a number change between an exploratory cell and the paper?

The project keeps a distinction between **442 observed weeks** used for description and a **469-week prepared grid** used for regular time-series alignment. Older notebook outputs sometimes used the latter in descriptive statistics; the repaired notebooks and final research report explicitly separate those purposes.

## Research results and model tuning

The paper-facing fixed-alpha benchmark is preserved so the report and slides remain reproducible. Some original selections were informed by the holdout, and therefore cannot support a clean claim of independently validated model superiority. The repaired notebook also demonstrates training-only time-series cross-validation for hyperparameter selection; it is documented separately rather than silently rewriting the paper result.

## Recommended checks before the presentation

1. Run `python scripts/verify_data.py`.
2. Execute the six notebooks in numerical order using **Restart Kernel and Run All Cells**.
3. Check figures and model errors against `docs/RUN_ALL_VALIDATION.txt` and `docs/RESEARCH_NOTES.md`.
4. Open `dashboard/Weekly_Mortality_Tableau.twbx` with your installed Tableau Desktop version and confirm its charts render.
5. Use `docs/SOURCE_CROSS_REFERENCE.md` to navigate from presentation slides to notebook sections and cells.
