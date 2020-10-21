user = {
  'name': 'Jude',
  'password': 'qwes123',
  'age': 26
}

for key in user:
  print(key)
print()

# iterate over the key and value
for key, value in user.items():
  print(f'{key}:{value}')
print()

  # iterate over the values
for value in user.values():
  print(f'{value}')
print()

  # iterate over the keys
for key in user.keys():
  print(key)

# Remember
# items() method returns a view that is formatted like a list of tuples
# so what you are doing is using that view to extract the keys and the values
print(user.items()) #=> dict_items([('name', 'Jude'), ('password', 'qwes123'), ('age', 26)])