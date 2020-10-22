try:
  4 / 0
except ZeroDivisionError as er:
  print(er)
else:
  print('This is a good division.')

try:
  4 / 8
except ZeroDivisionError as er:
  print(er)
else:
  print('This is a good division.')