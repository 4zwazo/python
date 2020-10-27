try:
  with open('sample.txt') as file_handler:
    # reading the file line by line
    for line in file_handler:
      print(line)
except FileNotFoundError as fnf:
  print(fnf)

# reading the entire file into memory
try:
  with open('sample.txt') as file_handler:
    # reading the file line by line
    lines = file_handler.readlines()
    for line in lines:
      print(line)
except FileNotFoundError as fnf:
  print(fnf)