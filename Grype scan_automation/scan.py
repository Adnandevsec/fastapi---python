import json
import pandas as pd

with open("results.json", "r", encoding="utf-8") as f:
  data = json.load(f)


rows = []

for match in data["matches"]:

    package = match["artifact"]["name"]
    version = match["artifact"]["version"]

    cve = match["vulnerability"]["id"]
    severity = match["vulnerability"]["severity"]

    rows.append({
        "Package": package,
        "Version": version,
        "CVE": cve,
        "Severity": severity
    })

print(rows[:5])

df = pd.DataFrame(rows)

df.to_excel(
    "grype_report.xlsx",
    index=False
)

print("Excel report generated successfully")