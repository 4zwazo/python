'''
  open(file,mode='r',buffering=-1,encoding=None,errors=None,newline=None, closefd=True, opener=None)
  open a file
'''

try:
  file_handler = open('sample.txt', encoding='utf8')
except:
  # ignore the error
  pass
finally:
  file_handler.close()

# using context manager to open the file
try:
  with open('example1.txt') as file_handler:
    for line in file_handler:
      print(line)
except FileNotFoundError as identifier:
  pass

