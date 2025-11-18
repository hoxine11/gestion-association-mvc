import csv
from typing import List, Dict

def read_csv(filepath: str) -> List[Dict]:
    try:
        with open(filepath, mode="r", newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []

def write_csv(filepath: str, data: List[Dict]):
    if not data:
        return

    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
