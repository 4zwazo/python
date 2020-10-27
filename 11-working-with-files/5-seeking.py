with open('example.txt') as file_handler:
  file_handler.seek(6)
  chunk = file_handler.read()
  print(chunk)