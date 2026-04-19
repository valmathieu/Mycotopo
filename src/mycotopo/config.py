"""Project-wide configuration: paths and environment-loaded settings."""
from __future__ import annotations

import os
from pathlib import Path

PROJECT_ROOT: Path = Path(__file__).resolve().parents[2]

DATA_DIR: Path = Path(os.getenv("MYCOTOPO_DATA_DIR", PROJECT_ROOT / "data"))
RAW_DIR: Path = DATA_DIR / "raw"
PROCESSED_DIR: Path = DATA_DIR / "processed"
PERIMETER_DIR: Path = DATA_DIR / "perimeter"

DUCKDB_PATH: Path = DATA_DIR / "mycotopo.duckdb"

# Default CRS conventions (see ROADMAP.md)
STORAGE_CRS: str = "EPSG:4326"
COMPUTATION_CRS: str = "EPSG:2154"