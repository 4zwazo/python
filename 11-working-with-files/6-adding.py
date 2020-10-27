with open('sample.txt', 'a') as file_handler:
  file_handler.write('Life is cool')

with open('sample.txt') as file_handler:
  text = file_handler.read()
  print(text)