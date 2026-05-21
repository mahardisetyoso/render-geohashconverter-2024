# Geohash Converter

A Streamlit-based web application for converting geographic coordinates and polygons into [geohashes](https://en.wikipedia.org/wiki/Geohash), with interactive map visualization and multi-format export (CSV / GeoJSON).

🔗 **Live demo:** [your-app.onrender.com](https://your-app.onrender.com) *(replace after deploy)*

---

## Why This Tool

In ride-hailing, logistics, and on-demand services, **geohash** is the lingua franca for spatial indexing — it converts continuous lat/long coordinates into discrete grid cells that are cheap to query, fast to compare, and trivial to aggregate. Despite how widely it's used, day-to-day operational workflows still rely on a patchwork of scripts and notebooks.

This tool consolidates the most common geohash workflows into a single UI — no Python notebook, no CLI, no QGIS plugin chain.

---

## Features

| # | Feature | Input | Output |
|---|---|---|---|
| 1 | **Copy Coordinates** | Lat/long string (comma-separated) | Geohash list + map preview + CSV/GeoJSON |
| 2 | **Draw Polygon** | Polygon drawn directly on a Folium map | Geohash list covering the polygon |
| 3 | **Bulk Extraction** | Uploaded GeoJSON file (single polygon) | Batch geohash conversion → CSV/GeoJSON |
| 4 | **GeoJSON → CSV Coordinates** | GeoJSON file | Flattened lat/long CSV |
| 5 | **Geohash Visualization by Copying** | Comma-separated geohash list | Map overlay showing coverage |
| 6 | **GeoJSON Cleaner (Single Polygon)** | Raw GeoJSON | Normalized single-polygon GeoJSON |
| 7 | **GeoJSON Cleaner (Multiple Polygons)** | Raw GeoJSON with multiple features | Cleaned multi-polygon GeoJSON |

All outputs are downloadable as CSV or GeoJSON.

---

## Tech Stack

- **Frontend / App framework:** Streamlit
- **Mapping:** Folium + streamlit-folium
- **Geospatial processing:** GeoPandas, Shapely
- **Geohash engine:** polygeohasher
- **Deployment:** Render (free tier compatible)

---

## Run Locally

```bash
# 1. Clone
git clone https://github.com/<your-username>/render-geohashconverter-2024.git
cd render-geohashconverter-2024

# 2. (Recommended) Create virtual environment
python -m venv .venv
source .venv/bin/activate     # Linux/Mac
# .venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run
streamlit run app.py
```

App opens at `http://localhost:8501`.

---

## Deploy to Render

1. Push this repository to your own GitHub account.
2. In [Render](https://render.com), create a new **Web Service** and connect your repo.
3. Configure the service as follows:

   | Setting | Value |
   |---|---|
   | **Environment** | Python 3 |
   | **Build Command** | `pip install -r requirements.txt` |
   | **Start Command** | `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.enableCORS=false` |

4. (Optional but recommended) Add a `runtime.txt` file with `python-3.10.13` to lock the Python version.

> ⚠️ **Note:** Render's free tier spins down after ~15 minutes of inactivity. First request after idle takes ~30 seconds to wake up.

---

## Use Cases

- **Ride-hailing & logistics ops:** Define service zones / coverage areas as geohash sets for fast spatial joins against driver and order data.
- **Map operations & QA:** Convert irregular operational polygons into discrete grid cells for systematic quality checks.
- **Geospatial analytics:** Bin point-level data into geohash cells for heatmaps, supply/demand analysis, and incident clustering.

---

## Project Structure

```
.
├── app.py                              # Landing page (intro + demo videos)
├── newdraw.py                          # Custom Folium Draw plugin wrapper
├── requirements.txt
├── styles/
│   └── main.css
├── assets/                             # Demo videos & images
└── pages/
    ├── Copy_Coordinates.py
    ├── Drawing_Polygon.py
    ├── Bulk_Extraction.py
    ├── GeoJSON_to_csv_Coordinates.py
    ├── Geohash_Visualization_by_Copying.py
    ├── Geojson_Cleaner_Single_Polygon.py
    ├── Geojson_Cleaner_for_Multiple_Polygon.py
    └── Personal_Information.py
```

---

## Known Limitations

- Bulk extraction expects GeoJSON files to be **dissolved into a single polygon/attribute** beforehand — use the GeoJSON Cleaner pages first if your file contains multiple features.
- Geohash precision range supported: **1–12**. Higher precision = smaller cell = larger output volume; values > 8 can be slow on free-tier hosting.
- The free tier of Render has cold starts; do not rely on this for production-critical workflows.

---

## Author

**Mahardi Wibowo** — Product Operations & Geospatial, ex-Grab (Central Map Operations, ~8 years). Currently focusing on geospatial analytics and data-driven ops automation.

- LinkedIn: [linkedin.com/in/<mahardisetyoso>](https://linkedin.com/in/mahardisetyoso)
- GitHub: [github.com/<mahardisetyoso](https://github.com/mahardisetyoso)

---

## License

MIT — see [LICENSE](LICENSE) for details. *(Add a LICENSE file if you intend to keep this MIT.)*