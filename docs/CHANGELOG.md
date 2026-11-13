# Corrections made to the six supplied notebooks

- **Notebook 1:** aligned scope with paper and actual regression deliverables; removed unimplemented classification objective and pre-assumed causal U-curve.
- **Notebook 2:** repaired datetime conversion after interpolation (`.dt` now works); added 469×13, continuity, null and duplicate assertions.
- **Notebook 3:** all descriptive counts based on 442 observed weeks; SQL temperature jump now joins genuine consecutive calendar weeks.
- **Notebook 4:** observed-only EDA and correlation; K-Means cluster names changed to descriptive mortality groups (not medically validated risk).
- **Notebook 5:** descriptive yearly totals and plots use observed table; decomposition uses the prepared regular grid; removed invalid claim of confirmed U/J-shaped causal risk.
- **Notebook 6:** removed redundant summer dummy from month-coded interaction OLS; changed exploratory Ridge/Lasso alpha selection to training-only time-series CV; retained original paper-aligned fixed-alpha comparison separately and verified 94 observed test labels.
- **Notebooks 2–6:** replaced `paper_support`-only path assumptions with a search of colocated files and original nested folders; included the regional CSV and geometry needed for Figure 5.
- **All notebooks:** standardized Python 3 kernel metadata, removed stale cached outputs before verified reruns, added auditable assertions.

The fixed-alpha paper results should not be misrepresented as an untouched independent model selection. Training-only CV estimates are separate from that report-replication section.

- Notebook 5 Figure 5: added a conditional, kernel-targeted Shapely installation fallback to prevent `ModuleNotFoundError: No module named shapely` on new Jupyter environments. No change to data, figure logic, cell numbering, or model results.
