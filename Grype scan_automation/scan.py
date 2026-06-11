import json
import pandas as pd
#here pandas will Create tables ,Export Excel, analyze data

with open("results.json", "r", encoding="utf-8") as f:
  #here will create a json file with reading mode
  data = json.load(f)
#convert the {match} to python dictionary

rows = []
# this to collect all vulns here

for match in data["matches"]:
# will pass through each vuln one by one
    package = match["artifact"]["name"]
#return the package name
    version = match["artifact"]["version"]
#return the current version
    cve = match["vulnerability"]["id"]
#return the cve number
    severity = match["vulnerability"]["severity"]
#return the severity
    rows.append({
        "Package": package,
        "Version": version,
        "CVE": cve,
        "Severity": severity
    })



df = pd.DataFrame(rows) 
# convert to table

df.to_excel(
    "grype_report.xlsx",
    index=False
)
# convert the table into excel

print("Excel report generated successfully")