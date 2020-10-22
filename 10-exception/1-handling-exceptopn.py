# bad: bare exception: bccause except has no type
try:
  with open('example.txt') as file_handler:
    for line in file_handler:
      print(line)
except:
  print('An error occurred')

# good: stating the exception you are catchign
try:
  with open('example.txt') as file_handler:
    for line in file_handler:
      print(line)
except OSError:
  print('An error occurred')
except ImportError:
  print('Unknown import')

# rewrite the exception
try:
  with open('example.txt') as file_handler:
    for line in file_handler:
      print(line)
except (OSError, ImportError):
  print('An error occurred')
