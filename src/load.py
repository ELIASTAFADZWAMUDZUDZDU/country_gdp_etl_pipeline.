import time
from pathlib import Path

from src.logger import log, time_log
from src.config import OUTPUT_CSV_PATH


def save_to_csv(df, file_path: str = OUTPUT_CSV_PATH) -> None:
    log("LOAD STARTED")
    start = time.perf_counter()

    output_path = Path(file_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    time_log("LOAD", start)
    print(f"Data successfully loaded to {output_path}")