try:
  with open('example.pdf', 'rb') as file_handler:
    file_contents = file_handler.read()
    print(file_contents)
except FileNotFoundError as identifier:
  pass