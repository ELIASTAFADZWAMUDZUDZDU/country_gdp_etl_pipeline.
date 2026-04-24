# Country GDP ETL Pipeline

Simple Python ETL pipeline that extracts GDP data, transforms it into multiple currencies, and loads results to CSV and SQLite.

## Project Structure

- `main.py` - Orchestrates the ETL flow.
- `src/extract.py` - Extracts country GDP data from the archived Wikipedia page.
- `src/transform.py` - Converts GDP values into USD/GBP/EUR/INR (billions).
- `src/load.py` - Writes final dataset to CSV.
- `src/database.py` - Loads data to SQLite and runs a query.
- `src/logger.py` - Appends pipeline logs to `logs/investment_log.txt`.

## Requirements

- Python 3.10+
- Dependencies from `requirements.txt`

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Outputs

- CSV: `data/FINAL_LIST.csv`
- SQLite DB: `FINAL.db` with table `countries_gdp`
- Log file: `logs/investment_log.txt`

## Notes

- The extractor uses HTTPS verification by default.
- The transformation step uses fallback FX rates if the exchange-rate API is unavailable.
