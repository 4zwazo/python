try:
  with open('strangefile.txt') as file_handler:
    for line in file_handler:
      print(line)
except OSError as err:
  print('An error has occurred')