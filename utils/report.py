import json
import os

def save_report(results):
    if not os.path.exists("reports"):
        os.makedirs("reports")
    file_path = "reports/report.json"

    with open(file_path, "w") as f:
        json.dump(results, f, indent=4)

        print(f"[*] Report saved to {file_path}")

