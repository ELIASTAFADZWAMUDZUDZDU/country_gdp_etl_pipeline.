import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

from src.logger import log, time_log


def extract_data(url):
    log("EXTRACTION STARTED")
    start = time.perf_counter()

    countries = []

    r = requests.get(url, timeout=10)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.find("table", class_="wikitable")
    rows = table.find_all("tr")

    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 3:
            name = cols[0].text.strip()
            try:
                gdp = float(cols[2].text.strip().replace(",", ""))
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