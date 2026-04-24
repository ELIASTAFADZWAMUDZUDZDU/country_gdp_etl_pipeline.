from datetime import datetime
import time

def log(msg):
    with open("logs/investment_log.txt", "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")

def time_log(stage_name, start_time):
    elapsed = time.perf_counter() - start_time
    log(f"{stage_name} completed in {elapsed:.2f} seconds")