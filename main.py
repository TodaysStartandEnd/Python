## Loop : for
files = ("main", "stack", "queue", "deque.py")
python_files = []

for file in files:
    if not file.endswith(".py") :
      python_files.append(f"{file}.py")
    else :
      python_files.append(file)

for file in python_files:
  print(f"{file} \n")