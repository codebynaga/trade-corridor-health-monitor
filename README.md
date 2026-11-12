# Trade Corridor Health Monitor

### Turning global trade data into supply chain risk intelligence

**An interactive decision-support dashboard combining structural trade exposure, historical trends, and machine-learning forecasts to examine 50 bilateral trade corridors across 2000–2024.**

**[Explore the live dashboard](https://codebynaga.github.io/trade-corridor-health-monitor/)** · **[View the source dataset](https://www.kaggle.com/datasets/sergionefedov/global-supply-chain-and-trade-disruptions-25-years)**

> **Project status:** Historical research and portfolio demonstration—not a live monitoring service, investment signal, or production-grade forecast engine. The published dashboard contains a fixed snapshot of analysis outputs.

---

## 1. The problem: why trade corridors matter

Global supply chains depend on trade connections between countries. Changes in freight conditions, tariffs, commodity markets, disruptions, and industry dependencies can alter how resilient those connections are. Yet trade value alone cannot tell a planner whether a corridor is vulnerable, and a corridor's structural vulnerabilities do not necessarily mean its trade will decline next year.

This project asks two complementary questions:

- **Structural exposure:** Which corridors appear more exposed to concentration, volatility, and industry vulnerability?
- **Growth direction:** Based on historical patterns, what next-year trade-growth direction does a supervised model estimate?

The goal is to make these two perspectives easy to compare—without confusing *exposure* with *predicted contraction*.

## 2. Who might use it—and for what?

| Stakeholder | Illustrative decision | Dashboard contribution |
| --- | --- | --- |
| Supply chain strategy | Which trade lanes deserve a deeper resilience review? | Compare relative structural exposure across corridors |
| Procurement and sourcing | Where might supplier diversification merit investigation? | Surface concentration and vulnerability indicators |
| Logistics and network planning | Which lanes should be included in contingency scenarios? | Examine exposure alongside historical trade dynamics |
| Business intelligence teams | How can disparate trade indicators be communicated? | Consolidate trends, scorecards, forecasts, and corridor drill-downs |
| Researchers and analysts | Are vulnerability and future growth closely related? | Evaluate the two lenses separately and inspect validation findings |

**Example workflow:** A planner filters for a sector, reviews the most exposed corridors, compares their recent growth patterns and model estimates, and selects a shortlist for deeper qualitative investigation. The dashboard **does not** automatically recommend suppliers, routes, or procurement actions.

## 3. What the dashboard contains

| View | What it helps answer |
| --- | --- |
| **Overview** | How has the selected corridor panel evolved, and where are the major patterns? |
| **Structural Exposure** | Which corridors rank higher on the project's relative exposure scorecard? |
| **Growth Direction** | What next-year growth estimates does the ML model produce, and how reliable were historical tests? |
| **Findings & Validation** | What did the analysis reveal, and where should results be interpreted cautiously? |
| **Corridor Explorer** | How do individual corridors compare by sector, exposure, and forecast characteristics? |

The **Obsidian & Copper** interface includes responsive layouts, a schematic corridor-network visualization, filters, light/dark themes, and corridor-table CSV export. The network connects approximate country/region centroids; **it is not a shipping-route or geographic-distance model**.

## 4. Analytical framework: two distinct lenses

### A. Structural exposure scorecard

The project combines percentile-based indicators related to corridor importance, concentration, volatility, and industry vulnerability into an **analyst-designed relative scorecard**. This helps prioritize corridors for review within the selected sample.

**Interpretation:** A higher exposure score indicates greater relative exposure under this scoring framework—not a calibrated probability of disruption, loss, or failure. Scores are comparative and depend on the included corridors and indicator definitions.

### B. Machine-learning growth forecasting

The supervised learning task estimates **next-year percentage trade growth** using historical corridor-level information. The project compares:

- **Ridge Regression:** A regularized linear benchmark.
- **Random Forest:** A nonlinear ensemble model.
- **Gradient Boosting:** A sequential tree-based ensemble; the model associated with the reported test metrics below.
- **Naive baseline:** A simple benchmark to test whether added model complexity delivers value.

The original analysis used a chronological split: **training through 2019, validation in 2020–2021, and testing in 2022–2023**. The 2024 data supports the latest historical dashboard view and prospective estimates; those prospective estimates are not verified future outcomes.

A supplementary hyperparameter-validation helper was revised to use **calendar-year-grouped expanding-window folds** rather than splitting observations from the same year across folds. This code change has unit tests but has **not** been independently rerun against the source CSVs.

### Reported historical model performance

| Test metric | Gradient Boosting | Naive baseline |
| --- | ---: | ---: |
| Mean Absolute Error (percentage points) | **6.747** | 12.710 |
| Root Mean Squared Error | **20.942** | 37.420 |
| R² | **0.124** | −1.798 |

The reported MAE is approximately **47% lower** than the naive benchmark. That is a useful comparison, but **R² remains modest**, meaning much of the variation in growth is not explained. Forecast errors can be substantial, especially around unusual events. These figures come from saved project artifacts and **have not been independently reproduced**; a separate saved diagnostic reported a different MAE and should be reconciled in a clean rerun.

**Important distinction:** Structural exposure and predicted growth are not interchangeable. A vulnerable corridor may still grow; a relatively less exposed corridor may contract. This project is designed to show both dimensions rather than collapse them into one misleading prediction.

## 5. Data and coverage

**Source:** [Global Supply Chain & Trade Disruptions — 25 Years](https://www.kaggle.com/datasets/sergionefedov/global-supply-chain-and-trade-disruptions-25-years), published on Kaggle by **sergionefedov**.

The original project works with **50 selected bilateral corridors over 2000–2024**, combining six categories of input data:

1. Trade flows
2. Shipping rates
3. Tariff timelines
4. Commodity prices and supply-chain conditions
5. Disruption events
6. Industry exposure

This is **not a complete census of global trade**. The source dataset's licensing, actual-versus-synthetic status, field definitions, and archive-to-notebook schema alignment still require independent verification. Raw CSVs are not distributed in this repository.

## 6. Technology and project architecture

- **Analysis:** Python, pandas/scikit-learn workflow in a Jupyter notebook
- **Modeling:** Ridge Regression, Random Forest, Gradient Boosting, baseline comparison
- **Validation:** Chronological holdouts and a year-grouped walk-forward helper
- **Visualization:** Self-contained HTML/CSS/JavaScript dashboard with embedded historical outputs
- **Hosting:** GitHub Pages; no live API or backend required

### Repository files

The GitHub upload currently places the files in the **repository root**, rather than retaining the intended package folders. The key published files are:

- [`index.html`](index.html) — live dashboard entry point
- [`trade_corridor_analysis.ipynb`](trade_corridor_analysis.ipynb) — source analysis notebook
- [`requirements.txt`](requirements.txt) and [`pyproject.toml`](pyproject.toml) — Python environment metadata
- [`download_data.py`](download_data.py) — Kaggle dataset retrieval helper
- [`validation.py`](validation.py) and [`test_validation.py`](test_validation.py) — validation utility and tests
- [`METHODOLOGY.md`](METHODOLOGY.md), [`LIMITATIONS.md`](LIMITATIONS.md), and [`RELEASE_CHECKLIST.md`](RELEASE_CHECKLIST.md) — supporting documentation

> **Developer note:** The downloadable project package originally organizes these files into `dashboard/`, `notebooks/`, `scripts/`, `src/`, `tests/`, and `docs/`. To run the analysis from a fresh clone, restore that folder structure or update the notebook's relative paths and imports accordingly. The live dashboard itself works independently as a static HTML page.

## 7. How to explore the project

**For a quick review:** Open the [live dashboard](https://codebynaga.github.io/trade-corridor-health-monitor/), move through the five sections, select a sector, and use Corridor Explorer to compare entries.

**For technical review:** Read the notebook and methodology, inspect the feature construction and time-based splits, and review the validation limitations before relying on the performance metrics.

**For reproduction:** Download the Kaggle dataset, verify its six required CSV filenames and schemas, restore the original repository folder layout, install the project dependencies, and rerun the notebook. The dashboard is **not automatically regenerated** when the notebook runs.

## 8. Key takeaways and business interpretation

- **Exposure is not destiny.** Structural vulnerability should inform resilience review, not be interpreted as a direct forecast of declining trade.
- **Forecasting adds a second perspective.** Historical model comparisons suggest potential value beyond a simple baseline, but explanatory power remains limited.
- **Prioritization is the practical use case.** A combined view can help analysts decide where to investigate further—not replace commercial judgment or scenario analysis.
- **Historical context matters.** Disruptions and structural shifts make long-range generalization challenging; forecasts should be monitored and refreshed before operational use.

## 9. Roadmap: what a production version would require

The following are **future opportunities, not implemented features**:

- **Verified and refreshed data:** Confirm source provenance, licensing, schemas, and a repeatable ingestion process.
- **Stronger forecasting evaluation:** Reconcile saved metrics, audit feature availability, expand walk-forward backtesting, and quantify uncertainty.
- **Explainability:** Add carefully interpreted feature-attribution and forecast-error diagnostics.
- **Scenario analysis:** Test hypothetical tariff, freight, or disruption shocks with explicitly stated assumptions.
- **Operationalization:** Automate data updates, retraining, monitoring, and dashboard generation, with appropriate quality checks.
- **Decision integration:** Connect outputs to a documented corridor-review workflow rather than treating scores as automated recommendations.

## 10. Limitations and responsible use

This is a **historical research prototype**. The dashboard does not update in real time, perform causal inference, or forecast shipping routes. Its scores are relative indicators rather than probabilities. Its model results require source-data verification and a clean reproducibility run; the dataset may contain synthetic or estimated fields. Do not use the outputs alone to make procurement, investment, or operational decisions.

## Credits and rights

Originally developed as a **group data science project**. Original contributors should be credited and publication permissions confirmed. The underlying dataset is attributed above; its redistribution terms should be verified. No software license is implied by publication of this repository.

---

**The central idea:** *Trade corridor resilience and trade growth are related business questions, but they are not the same analytical problem. Better decisions start by examining both.*
