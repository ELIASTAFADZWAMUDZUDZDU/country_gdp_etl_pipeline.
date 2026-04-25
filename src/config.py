WIKI_GDP_URL = (
    "https://web.archive.org/web/20230902185326/"
    "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
)

FX_API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

OUTPUT_CSV_PATH = "data/FINAL_LIST.csv"
OUTPUT_DB_PATH = "FINAL.db"
LOG_FILE_PATH = "logs/investment_log.txt"
DB_TABLE_NAME = "countries_gdp"

FX_FALLBACK_RATES = {
    "GBP": 0.79,
    "EUR": 0.92,
    "INR": 83.0,
}
