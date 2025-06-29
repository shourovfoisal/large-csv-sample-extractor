import os

def writefile(data):
  os.makedirs("jsonoutpure", exist_ok=True)
  file_path = os.path.join("jsonoutpure", "out.json")
  with open(file_path, "w", encoding="utf-8") as outfile:
      outfile.writelines(data)
      outfile.write("\n")