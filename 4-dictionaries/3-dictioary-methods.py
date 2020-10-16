a_emp_dict = {
  'first_name': 'jude',
  'last_name': 'ti cool',
  'email': 'ticool@gmail.com'
}

# get a key value
print(a_emp_dict.get('last_name'))

# return default value if key not found
print(a_emp_dict.get('house'))
print(a_emp_dict.get('house', 'Not Found'))

# clear the dictionary
a_emp_dict.clear()
print(a_emp_dict)

a_emp_dict = {
  'first_name': 'jude',
  'last_name': 'ti cool',
  'email': 'ticool@gmail.com'
}

# create a shallow copy
b_emp_dict = a_emp_dict.copy()
print(a_emp_dict)
print(b_emp_dict)

# get a view of the dictionary items
new_dict = a_emp_dict.items();
print(new_dict)

# get a view of the dictionary keys
key_dict = a_emp_dict.keys()
print(key_dict)

# get a view of the dictionary values
val_dict = a_emp_dict.values()
print(val_dict)

# remove a key from the dictionary
remove_val = a_emp_dict.pop('first_name')
print(remove_val)

# return the key/val removed
remove_key_val = a_emp_dict.popitem()
print(remove_key_val)

# update/overwrite the dictionary
first_name = ('first_name', 'jude')
a_emp_dict.update([('middle', 'menard')])
a_emp_dict.update([first_name])
print(a_emp_dict)

