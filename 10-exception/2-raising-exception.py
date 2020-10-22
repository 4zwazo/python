# b = -1

# if b < 0:
#   raise Exception('Invalid operation...')

# x = 0

# try:
#   9 / x
#   raise Exception('Invalid operation...')
# except Exception:
#     print('An error occurred')

try:
  raise FileNotFoundError('Bad file')
except FileNotFoundError as error:
  print(type(error))
  print(error.args)
  print(error)