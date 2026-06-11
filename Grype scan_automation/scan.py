import json

with open("results.json", "r", encoding="utf-8") as f:
  data = json.load(f)

print(data.keys())