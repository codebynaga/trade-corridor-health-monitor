# Interactive dashboard — v2.0

Open `index.html` in a modern browser, or publish the repository through GitHub Pages at `/dashboard/`. The dashboard is a static, self-contained HTML document with embedded historical notebook outputs. No API key, server, or external charting library is required; Google Fonts are optional.

## Features
- Executive overview with a historical-data disclosure and a schematic geographic corridor network.
- Click or keyboard-select routes to inspect trade value, exposure score, and forecast growth.
- Filter the map by sector; color connections by exposure or predicted growth.
- Dark/light theme toggle, with optional browser-local preference persistence.
- Structural exposure, growth modeling, validation findings, and searchable corridor explorer.
- Download the currently filtered corridor explorer rows as CSV.
- Responsive layout for mobile and desktop, reduced-motion accessibility support.

## Important limitations
- The map is **schematic**, using approximate country/region centroids and decorative land shapes. It is not a GIS basemap, shipping route or geographic distance model.
- Forecasts are historical notebook outputs, not predictions refreshed in the browser.
- The map only draws corridors with recognized endpoints. The corridor explorer retains all 50 entries.
- Model metrics should be verified by rerunning the supplied notebook against the source data.
- Check the Kaggle dataset's license before redistribution of the embedded data.
