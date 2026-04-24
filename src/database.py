import sqlite3
import time
import pandas as pd

from src.logger import log, time_log


def save_to_database(df, db_path="FINAL.db"):
    log("DATABASE LOAD STARTED")
    start = time.perf_counter()

    conn = sqlite3.connect(db_path)
    df.to_sql("countries_gdp", conn, if_exists="replace", index=False)
    conn.close()

    time_log("DATABASE LOAD", start)
    print("Table successfully created in SQLite database")


def run_query(db_path="FINAL.db"):
    conn = sqlite3.connect(db_path)

    result = pd.read_sql(
        """
        SELECT COUNTRY_NAME, GDP_USD_BILLION
        FROM countries_gdp
        WHERE GDP_USD_BILLION > 100
        ORDER BY GDP_USD_BILLION DESC
        """,
        conn,
    )

    conn.close()
    return result
# src/database.py
import sqlite3
import time
import pandas as pd

from src.logger import log, time_log


def save_to_database(df, db_path="FINAL.db"):
    log("DATABASE LOAD STARTED")
    start = time.perf_counter()

    conn = sqlite3.connect(db_path)
    df.to_sql("countries_gdp", conn, if_exists="replace", index=False)
    conn.close()

    time_log("DATABASE LOAD", start)
    print("Table successfully created in SQLite database")


def run_query(db_path="FINAL.db"):
    conn = sqlite3.connect(db_path)

    result = pd.read_sql(
        """
        SELECT COUNTRY_NAME, GDP_USD_BILLION
        FROM countries_gdp
        WHERE GDP_USD_BILLION > 100
        ORDER BY GDP_USD_BILLION DESC
        """,
        conn,
    )

    conn.close()
    return result