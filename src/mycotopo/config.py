"""Project-wide configuration: paths and environment-loaded settings."""
from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT: Path = Path(__file__).resolve().parents[2]

# Load .env from project root if present (noop in production / CI).
load_dotenv(PROJECT_ROOT / ".env")

# ── Paths ────────────────────────────────────────────────────
DATA_DIR: Path = Path(os.getenv("MYCOTOPO_DATA_DIR", PROJECT_ROOT / "data"))
RAW_DIR: Path = DATA_DIR / "raw"
PROCESSED_DIR: Path = DATA_DIR / "processed"
PERIMETER_DIR: Path = DATA_DIR / "perimeter"
DUCKDB_PATH: Path = DATA_DIR / "mycotopo.duckdb"

# ── CRS conventions (see ROADMAP.md) ─────────────────────────
STORAGE_CRS: str = "EPSG:4326"
COMPUTATION_CRS: str = "EPSG:2154"

# ── API keys (empty string = not configured) ─────────────────
METEO_FRANCE_API_KEY: str = os.getenv("METEO_FRANCE_API_KEY", "")
OPEN_METEO_API_KEY: str = os.getenv("OPEN_METEO_API_KEY", "")
IGN_API_KEY: str = os.getenv("IGN_API_KEY", "")

# ── FastAPI ──────────────────────────────────────────────────
API_HOST: str = os.getenv("MYCOTOPO_API_HOST", "127.0.0.1")
API_PORT: int = int(os.getenv("MYCOTOPO_API_PORT", "8000"))
CORS_ORIGINS: list[str] = [
    o.strip() for o in os.getenv("MYCOTOPO_CORS_ORIGINS", "").split(",") if o.strip()
]

# ── Logging ──────────────────────────────────────────────────
LOG_LEVEL: str = os.getenv("MYCOTOPO_LOG_LEVEL", "INFO").upper()