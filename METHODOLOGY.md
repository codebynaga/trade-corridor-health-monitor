# Methodology

## Research question
Monitor trade corridors through two separate lenses: (1) **structural exposure** — an analyst-designed, percentile-based scorecard of concentration, volatility and vulnerability; and (2) **growth direction** — supervised prediction of next-year percentage trade growth.

## Data and unit of observation
50 bilateral trade corridors, annual observations from 2000–2024 as reported by the original project dashboard. Inputs: trade flows, shipping rates, tariffs, commodity prices, disruptions and industry exposure. This is a *selected-corridor panel*, not the entire world trade economy.

## Models
Ridge Regression, Random Forest and Gradient Boosting compared with a naive baseline. The original notebook's model selection uses training observations through 2019, validation 2020–2021 and test 2022–2023. The selected model is refit on train+validation before test scoring. The 2024 panel is used for the latest dashboard view and prospective forecasts, not a verified realized outcome.

## Validation adjustment in this release
The original supplementary tuning section used row-based `TimeSeriesSplit` on year-sorted panel data, which can split a year between folds. The repository replaces it with `YearWalkForwardSplit`, which holds out complete calendar years. This change has **not** been re-evaluated on original CSVs. The original notebook outputs are cleared intentionally.

## Reported metrics and limitations
The submitted dashboard/notebook reported approximately 6.747 test MAE for Gradient Boosting vs 12.710 for the naive baseline, and R² approximately 0.124. These are *historical reported figures, not independently reproduced*. Other notebook diagnostic outputs showed a differing all-observations MAE; rerun and reconcile before treating either as canonical.

## Interpretation
The dashboard's historical association check found little alignment between structural exposure and next-year contraction. The two lenses are not interchangeable. No causal inference or real-time monitoring is claimed.
