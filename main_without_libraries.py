import csv
import json
from writefile import writefile


with open("input/test.csv", encoding="utf8", mode="r", newline="") as file:
  rows = csv.DictReader(file)
  
  limit=2
  data_array = []
  for index, item in enumerate(rows):
    if index == limit: break
    data_array.append(item)
  
  print(data_array)
  writefile("jsonoutpure", json.dumps(data_array))
  