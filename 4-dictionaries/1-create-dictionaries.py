# create an empty dict using dict constructor
my_dict = dict()
print(type(my_dict))

# a list
kv_list = [['key-1', 'value-1'], ['key-2', 'value-2']]
# convert list to dict
print(dict(kv_list))

# create a list using curly braces
a_emp_dict = {
  'first_name': 'jude',
  'last_name': 'ti cool',
  'email': 'ticool@gmail.com'
}

print(a_emp_dict)

#
a_emp_dict = dict(
  first_name='jude',
  last_name='ti cool',
  email='ticool@gmail.com'
)
print(a_emp_dict)

info_list = [
  ('first_name', 'Paul'),
  ('last_name', 'Jean'),
  ('email', 'paul@gmail.com')
]
print(dict(info_list))

