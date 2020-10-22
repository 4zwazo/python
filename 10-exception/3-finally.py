try:
  1/0
except ZeroDivisionError as er:
  print(er)
finally:
  print('cleaned up')