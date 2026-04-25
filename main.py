import time

from src.config import WIKI_GDP_URL
from src.extract import extract_data
from src.transform import transform_data
from src.load import save_to_csv
from src.database import save_to_database, run_query
from src.logger import log, time_log


def main() -> None:
    log("PIPELINE STARTED")
    start = time.perf_counter()

    try:
        df = extract_data(WIKI_GDP_URL)
        df = transform_data(df)

        save_to_csv(df)
        save_to_database(df)

        result = run_query(min_gdp_billion=100.0)
        print(result)

        log("PIPELINE COMPLETED SUCCESSFULLY")

    except Exception as e:
        log(f"PIPELINE FAILED: {e!r}")
        raise

    time_log("PIPELINE", start)


if __name__ == "__main__":
    main()