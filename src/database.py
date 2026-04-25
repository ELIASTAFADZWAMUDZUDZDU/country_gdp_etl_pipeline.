import sqlite3
import time
from pathlib import Path

import pandas as pd

from src.config import DB_TABLE_NAME, OUTPUT_DB_PATH
from src.logger import log, time_log


def save_to_database(df, db_path: str = OUTPUT_DB_PATH) -> None:
    log("DATABASE LOAD STARTED")
    start = time.perf_counter()

    db_file = Path(db_path)
    if db_file.parent != Path("."):
        db_file.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(db_file) as conn:
        df.to_sql(DB_TABLE_NAME, conn, if_exists="replace", index=False)

    time_log("DATABASE LOAD", start)
    print(f"Table successfully created in SQLite database: {db_file}")


def run_query(db_path: str = OUTPUT_DB_PATH, min_gdp_billion: float = 100.0) -> pd.DataFrame:
    query = f"""
        SELECT COUNTRY_NAME, GDP_USD_BILLION
        FROM {DB_TABLE_NAME}
        WHERE GDP_USD_BILLION > ?
        ORDER BY GDP_USD_BILLION DESC
    """

    with sqlite3.connect(db_path) as conn:
        result = pd.read_sql(query, conn, params=(min_gdp_billion,))

    return result