# Known limitations and publication gates

2. **Data provenance:** external licensing, actual-vs-synthetic status, and field-level methodology require verification by the original authors.
3. **Temporal feature availability:** verify each feature (especially any field labeled with a later year such as `nearshoring_score_2024`) was historically available at the prediction cutoff. It is not included in the visible model feature list, but enters the wider data pipeline.
5. **Post-hoc diagnostics:** outlier removal is a sensitivity analysis, not a replacement for full-sample performance.
6. **Snapshot dashboard:** HTML embeds frozen notebook outputs; it does not fetch new observations or make live model calls.
7. **Interpretability:** feature importance does not establish causal influence; scorecard labels are conventions, not calibrated probabilities.
8. **Coverage:** only selected 50 corridors; totals are not a global-trade census.
9. **Validation change:** year-grouped walk-forward CV has unit tests but no end-to-end rerun without data.
10. **Operational deployment:** no scheduled ingestion, drift monitoring, retraining, access controls, or SLA.
