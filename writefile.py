import os

def writefile(folder, data):
  os.makedirs(folder, exist_ok=True)
  file_path = os.path.join(folder, "out.json")
  with open(file_path, "w", encoding="utf-8") as outfile:
      outfile.writelines(data)
      outfile.write("\n")