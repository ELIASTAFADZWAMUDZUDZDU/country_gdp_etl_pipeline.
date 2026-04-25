from datetime import datetime
from pathlib import Path
import time

from src.config import LOG_FILE_PATH


def log(msg: str) -> None:
    log_file = Path(LOG_FILE_PATH)
    log_file.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with log_file.open("a", encoding="utf-8") as file:
        file.write(f"{timestamp} - {msg}\n")


def time_log(stage_name: str, start_time: float) -> None:
    elapsed = time.perf_counter() - start_time
    log(f"{stage_name} completed in {elapsed:.2f} seconds")