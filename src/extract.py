import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import re

from src.config import WIKI_GDP_URL
from src.logger import log, time_log


def _parse_gdp_million(raw_value: str) -> float:
    cleaned = re.sub(r"\[[^\]]*\]", "", raw_value)
    cleaned = cleaned.replace(",", "").strip()
    cleaned = cleaned.split(" ")[0]
    return float(cleaned)


def extract_data(url: str = WIKI_GDP_URL) -> pd.DataFrame:
    log("EXTRACTION STARTED")
    start = time.perf_counter()

    countries = []

    headers = {"User-Agent": "country-gdp-etl-pipeline/1.0"}
    r = requests.get(url, headers=headers, timeout=10)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.find("table", class_="wikitable")
    if table is None:
        raise ValueError("Could not find GDP table in source HTML.")
    rows = table.find_all("tr")

    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 3:
            name = cols[0].text.strip()
            try:
                gdp = _parse_gdp_million(cols[2].text.strip())
            except ValueError:
                continue

            countries.append({
                "COUNTRY_NAME": name,
                "GDP_MILLION": gdp
            })

    df = pd.DataFrame(countries)

    log(f"EXTRACTION completed with {len(df)} rows")
    time_log("EXTRACTION", start)

    return df