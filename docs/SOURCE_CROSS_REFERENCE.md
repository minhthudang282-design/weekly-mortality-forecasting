# Paper -> Slides -> Verified Notebooks: source cross-reference

This guide accompanies the **six repaired notebooks** tested with `Restart & Run All` on 2026-11-13. It applies to `slides/Weekly_Mortality_Full_Presentation.pptx` and `slides/Weekly_Mortality_10Min_Presentation.pptx`, **not** to earlier slide releases. All cell positions below are **1-based** positions in the complete `.ipynb`, including Markdown cells. The `§` references are more robust than cell numbers if someone adds cells.

| Slide(s) | Evidence to show | Notebook or artifact in this repository | Related paper |
|---|---|---|---|
| 3–5 | Research problem / related work / research gap | Notebook 1 §§1.1, 1.5, 1.7–1.10 | Introduction, Table 1, Method §4 |
| 7 | Research workflow | Notebook 1 §1.10; Notebook 2 §2.15; Notebook 6 §6.13 | Fig. 2, p. 4 |
| 8–9 | Data sources and cleaning | Notebook 2 §2.7.5 (cell 22), §2.15 (cell 45) | Table 2, pp. 3–4 |
| 10 | Violin plot by season | Notebook 5 §5.6 (cell 14) | Fig. 1, p. 3 |
| 11 | Temperature vs deaths scatter | Notebook 5 §5.3 (cell 8) | Fig. 3 / narrative, pp. 5–6 |
| 12–13 | SQL peak week | Notebook 3 §3.4 (cell 11) | Fig. 3, p. 5 |
| 14 | SQL seasonal averages | Notebook 3 §3.5 (cell 13) | RQ1, §5.1 |
| 15 | SQL weeks >25°C | Notebook 3 §3.6 (cells 15–16) | §5.1, limitations |
| 16 | SQL pre/during/post COVID | Notebook 3 §3.11 (cell 28 for three-phase summary) | §5.1 |
| 17 | SQL temperature jumps | Notebook 3 §3.10 (cell 25): join **dates exactly 7 days apart** | Exploratory SQL only |
| 19–23 | Python / EDA / time series | Notebook 4 §§4.2–4.7, 4.13; Notebook 5 §§5.6–5.13 | Figs. 1, 3–5 |
| 25–26 | Extra features before regression | Notebook 6 §6.2 (cell 6), §6.3 (cell 8), §6.13 (cell 29) | §4 / Table 2 |
| 27 | Forecast references | Notebook 6 §6.13 (cell 29, code lines 90–92) | Table 3, p. 7 |
| 28 | OLS | Notebook 6 §§6.4–6.7 (cells 10 and 16); §6.13 (cell 29) | Table 3, p. 7; discussion |
| 29 | Polynomial degree 2 | Notebook 6 §6.11 (cell 24); §6.13 (cell 29) | Table 3, p. 7 |
| 30 | Ridge degree 2 | Notebook 6 §§6.10–6.11 (cells 22, 24); §6.13 (cell 29) | Table 3, p. 7 |
| 31 | Lasso degree 2 | Notebook 6 §§6.10–6.11 (cells 22, 24); §6.13 (cell 29) | Table 3, p. 7 |
| 32 | Polynomial degree 3 complexity check | Notebook 6 §6.8 (cell 18), §6.13 (cell 29) | Table 3, p. 7 |
| 33–38 | Held-out accuracy, phase/ablation, robustness | Notebook 6 §6.13 (cell 29), final paper-aligned result table (cell 38) | Tables 3–5, Figs. 6–7 |
| 39 | Tableau dashboard | Separate `.twbx` artifact, not a notebook source | Dashboard implements paper findings |
| 40–41 | 3 RQs, limitations/future work | Notebook 6 §6.12–6.13; Notebook 1 §1.9 | Discussion / conclusion, pp. 9–10 |
| 42–43 | Human Delta / AI error #016 | **AI Audit Log.xlsx** in the Drive (not bundled); entry 016 | Report Tables 3 and 5 |

## Invariant numerical checks

- 442 actually observed weeks, total registered deaths 4,769,329.
- 469-week grid with 27 interpolated rows; 468 rows after lag-1, 374 train and 94 test.
- Pearson r (deaths versus mean weekly UK Tmax) approximately −0.474 on observed weeks.
- Polynomial degree-2 without temperature: 94-week held-out MAE ~643.94 deaths/week.
- Last-value reference MAE ~738.8, seasonal-naive reference ~703.4.
- Degree-two plus-temperature variants do not improve pooled MAE consistently; Holm-adjusted paired tests in the report do not confirm statistical superiority.

## Important distinctions

1. **Section headings remain anchored**, but old cell identifiers in previous slide versions went stale because the repaired notebooks include additional cells. Use the two presentations included in this repository.
2. The SQL temperature-jump comparison now uses a seven-day date join. Earlier slide screenshots showing a `ROWID` self-join are obsolete. The largest observed consecutive-week increase is +7.31°C.
3. The detailed Ridge/Lasso hyperparameter selection in the exploratory notebook uses training-only time-series cross-validation. **Report-matched fixed-alpha results** remain under Notebook 6 §6.13; don't claim that the published model-selection procedure was an untouched prospective holdout.
4. Screenshot code excerpts in the slides are **selected/simplified extracts**, not the full notebook cell. Follow the exact section number to demonstrate real code and outputs.
5. The report is distributed here as `report/Weekly_Mortality_Forecasting_Report.pdf` (the earlier Drive/local filenames were `Report(2).pdf` and `Report(2)(3).pdf`).
6. Notebook execution was verified in Python 3.13.5 with the provided files; as with any scientific code, this cannot guarantee identical behavior in every future environment.
