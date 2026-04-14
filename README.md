# Mycotopo

Interactive mapping application for mycological prospecting in France. Mycotopo cross-references open geographic data layers — forest species, soil types, hydrography, relief, and weather — to identify zones favorable to mushroom growth.

## MVP Scope

The MVP targets the **Chartreuse massif** (~35×15 km) with a single pilot species: **cèpe** (*Boletus edulis*). The compact, diverse terrain (beech, spruce, oak forests, 400–2000 m elevation) allows fast iteration before scaling to Savoie, then the full AURA region.

## How It Works

The scoring model combines two independent components:

- **Potential score** (static): intrinsic suitability of a zone based on forest species composition, soil type, proximity to watercourses, altitude, and slope aspect.
- **Conditions score** (dynamic): current weather favorability based on cumulative rainfall (10–15 days), day/night temperature differential, and season alignment.

The final score is `potential × conditions`, normalized to a 0–100 scale. Static spatial data is cached while weather modulation stays responsive.

## Tech Stack

| Layer           | Technology                            |
| --------------- | ------------------------------------- |
| Language        | Python 3.11+                          |
| Package manager | pixi (conda-forge)                    |
| Geospatial      | GeoPandas, Shapely, Rasterio, Fiona   |
| Database        | DuckDB + spatial extension            |
| Backend         | FastAPI                               |
| Frontend        | React + MapLibre GL JS (react-map-gl) |
| Notebooks       | Jupyter, Folium, Plotly, Matplotlib   |

## Data Sources

| Layer          | Source                       | Format         |
| -------------- | ---------------------------- | -------------- |
| Forest species | Carte forestière IGN v2      | SHP / GPKG     |
| Soil types     | INRAE / GIS Sol (1:250k)     | WFS / download |
| Hydrography    | BD TOPAGE (depts 38 + 73)    | GPKG           |
| Relief / DEM   | MNT IGN (RGE ALTI / BD ALTI) | GeoTIFF        |
| Weather        | Open-Meteo or Météo-France   | API            |

## Project Structure

```
mycotopo/
├── src/mycotopo/
│   ├── data/            # Download, parsing, cache of geo data
│   ├── domain/          # Scoring logic, layer cross-referencing
│   ├── api/             # FastAPI endpoints
│   └── config.py
├── frontend/            # React + MapLibre app
├── notebooks/           # Exploration and prototyping (Jupyter)
├── data/                # Local data cache (gitignored)
├── tests/
├── docs/
├── pixi.toml
├── pyproject.toml
├── Makefile
└── README.md
```

## Getting Started

### Prerequisites

- [pixi](https://pixi.sh) package manager

### Setup

```bash
git clone <repo-url>
cd mycotopo
pixi install
```

### Development

```bash
# Launch Jupyter notebooks
make notebook

# Run data pipeline (download, clip, store in DuckDB)
make data

# Start API server
make api

# Start frontend dev server
make frontend-dev

# Full-stack local run (API + built frontend)
make serve
```

## Development Phases

| Phase | Focus                                        | Status |
| ----- | -------------------------------------------- | ------ |
| 0     | Foundations — repo setup, literature review  | 🔲     |
| 1     | Data exploration on Chartreuse (6 notebooks) | 🔲     |
| 2     | Data pipeline & spatial joins (DuckDB)       | 🔲     |
| 3     | Scoring model for cèpe                       | 🔲     |
| 4     | FastAPI backend                              | 🔲     |
| 5     | React + MapLibre frontend                    | 🔲     |
| 6     | Field validation & geographic scale-up       | 🔲     |

## CRS Convention

- **Storage** (DuckDB): EPSG:4326 (WGS84) — matches MapLibre
- **Computation**: EPSG:2154 (Lambert-93) — for distances and areas
- Reprojection happens once at data import time

## Contributing

- Code follows PEP 8 with type hints and Google-style docstrings
- Conventional commits (`feat:`, `fix:`, `docs:`, `refactor:`)
- Tests via pytest
- Data is never committed — the pipeline handles downloads

## License

[GPL-3.0 license](https://github.com/valmathieu/Mycotopo#GPL-3.0-1-ov-file)
