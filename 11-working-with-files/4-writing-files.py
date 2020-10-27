try:
  with open('example.txt', 'w') as file_handler:
    file_handler.write('This is super cool')
except FileNotFoundError as identifier:
  pass