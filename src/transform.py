import time
import requests

from src.logger import log, time_log


def transform_data(df):
    log("TRANSFORMATION STARTED")
    start = time.perf_counter()

    df = df.copy()

    # fallback values if FX API fails
    GBP = 0.79
    EUR = 0.92
    INR = 83.0

    try:
        r = requests.get("https://api.exchangerate-api.com/v4/latest/USD", timeout=10).json()
        GBP = r["rates"]["GBP"]
        EUR = r["rates"]["EUR"]
        INR = r["rates"]["INR"]
    except requests.RequestException:
        log("FX API unavailable, using fallback rates")

    df["GDP_USD_BILLION"] = (df["GDP_MILLION"] / 1000).round(2)
    df["GDP_GBP_BILLION"] = (df["GDP_USD_BILLION"] * GBP).round(2)
    df["GDP_EUR_BILLION"] = (df["GDP_USD_BILLION"] * EUR).round(2)
    df["GDP_INR_BILLION"] = (df["GDP_USD_BILLION"] * INR).round(2)

    time_log("TRANSFORMATION", start)
    return df