import time

from src.extract import extract_data
from src.transform import transform_data
from src.load import save_to_csv
from src.database import save_to_database, run_query
from src.logger import log, time_log


URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"


def main():
    log("PIPELINE STARTED")
    start = time.perf_counter()

    try:
        df = extract_data(URL)
        df = transform_data(df)

        save_to_csv(df)
        save_to_database(df)

        result = run_query()
        print(result)

        log("PIPELINE COMPLETED SUCCESSFULLY")

    except Exception as e:
        log(f"PIPELINE FAILED: {e}")
        raise

    time_log("PIPELINE", start)


if __name__ == "__main__":
    main()