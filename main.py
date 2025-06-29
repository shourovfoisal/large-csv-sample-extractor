import os
import pandas as pd

df = pd.read_csv("input/test.csv", encoding="utf8", nrows=2)

os.makedirs("output", exist_ok=True)
df.to_csv("output/out.csv", index=False)

os.makedirs("jsonout", exist_ok=True)
df.to_json("jsonout/out.json", index=False, orient="records")