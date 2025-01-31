import os
import csv


def save_to_file(file_name, jobs):
    os.makedirs("data", exist_ok=True)
    with open(f"data/{file_name}.csv", "w", encoding="utf-8") as file:
        fieldnames = ["title", "company", "region", "link"]
        writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(jobs)
