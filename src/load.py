import time

from src.logger import log, time_log


def save_to_csv(df, file_path="data/FINAL_LIST.csv"):
    log("LOAD STARTED")
    start = time.perf_counter()

    df.to_csv(file_path, index=False)

    time_log("LOAD", start)
    print(f"Data successfully loaded to {file_path}")