import time
import requests

from src.config import FX_API_URL, FX_FALLBACK_RATES
from src.logger import log, time_log


def get_exchange_rates() -> dict:
    rates = FX_FALLBACK_RATES.copy()
    try:
        response = requests.get(FX_API_URL, timeout=10)
        response.raise_for_status()
        payload = response.json()
        rates["GBP"] = float(payload["rates"]["GBP"])
        rates["EUR"] = float(payload["rates"]["EUR"])
        rates["INR"] = float(payload["rates"]["INR"])
    except (requests.RequestException, KeyError, TypeError, ValueError):
        log("FX API unavailable or invalid response, using fallback rates")
    return rates


def transform_data(df):
    log("TRANSFORMATION STARTED")
    start = time.perf_counter()

    df = df.copy()
    rates = get_exchange_rates()

    df["GDP_USD_BILLION"] = (df["GDP_MILLION"] / 1000).round(2)
    df["GDP_GBP_BILLION"] = (df["GDP_USD_BILLION"] * rates["GBP"]).round(2)
    df["GDP_EUR_BILLION"] = (df["GDP_USD_BILLION"] * rates["EUR"]).round(2)
    df["GDP_INR_BILLION"] = (df["GDP_USD_BILLION"] * rates["INR"]).round(2)

    time_log("TRANSFORMATION", start)
    return df