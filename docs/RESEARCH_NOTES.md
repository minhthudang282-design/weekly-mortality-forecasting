# Reproducibility and interpretation notes

## Data and split

- Original merged observed dataset: **442 weekly observations**, **4,769,329 registered deaths** in the included observed weeks.
- Prepared calendar: **469 week rows** after adding 27 absent calendar weeks using interpolation.
- One-week lag creates **468 modelable rows**. The fixed chronological split uses **374 training** and **94 test** rows.
- The 94 held-out outcomes are from observed weeks, not the interpolated gap rows.
- Do not mix a prepared/interpolated dataset total with a total of observed death registrations.

## Notebook-to-result map

| Notebook | Evidence |
|---|---|
| 1. Business Understanding | Problem framing, study objective and research questions |
| 2. Data Collection, Understanding, and Preparation | Missing-week calendar, interpolation and variable engineering |
| 3. Data Analysis with SQL | Seasonal/yearly summaries, unusual weeks and consecutive-week temperature changes |
| 4. Data Analysis with Python | EDA, Pearson/Spearman, lag analysis and statistical checks |
| 5. Data Visualization | Seasonal, timeline, lag and regional-temperature plots |
| 6. Regression Analysis | Three baselines; OLS, Polynomial 2/3, Ridge 2, Lasso 2; MAE/RMSE/R²; ablation, DM + Holm |

See `SOURCE_CROSS_REFERENCE.md` for exact section/cell navigation from the accompanying slide deck.

## Main retrospective test results

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| OLS | 672.0 | 1051.2 | 0.166 |
| OLS + temperature | 668.4 | 1049.0 | 0.170 |
| Polynomial 2 | **643.9** | **939.0** | **0.335** |
| Polynomial 2 + temperature | 650.0 | 946.2 | 0.324 |
| Ridge 2 | 677.3 | 965.8 | 0.296 |
| Ridge 2 + temperature | 685.0 | 963.1 | 0.300 |
| Lasso 2 | **643.9** | **939.0** | **0.335** |
| Lasso 2 + temperature | 649.9 | 946.1 | 0.324 |

*These results are rounded from the project report, Table 3. They concern a single chronological test block and should not be represented as a statistically confirmed winner or as forecast accuracy guaranteed for future weeks.*

## What not to claim

1. A negative Pearson coefficient **does not** prove that cold weather causes the observed mortality changes.
2. The strongest correlation near a **two-week lag** is a descriptive result, **not a proven causal delay**.
3. Polynomial degree two does **not**, by itself, prove a temperature mortality U- or J-shape: the polynomial expansion includes mortality lags, month indicators and interactions.
4. A phase-specific lower MAE does **not** establish a clinical safe-temperature threshold.
5. A model with an observed temperature value for the target week is an **ex-post/retrospective** comparison, not a practical ahead-of-time weather-driven alert.
6. A lower mean MAE relative to a baseline is **not** the same as an established significant improvement; the report's twelve Holm-adjusted comparisons have no confirmed advantage.

## Selection and uncertainty

The paper-facing Ridge/Lasso comparisons include an original fixed-alpha benchmark; choices informed by the held-out period limit clean post-selection claims. The repaired notebook retains the paper benchmark for reproducibility while documenting training-only time-series cross-validation as a preferable selection method. Future work should use rolling-origin evaluation, independent validation and weather forecasts available at prediction time.

## Environment

`requirements.txt` describes the runtime dependencies, including `shapely`, used for the regional map. `RUN_ALL_VALIDATION.txt` documents a local fresh-kernel end-to-end execution on Python 3.13.5; other computers and future dependency versions may require installation or revalidation.
