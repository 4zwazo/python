# Using %s style
name = 'Pascal'
print('My name is %s' % name)

age = 18
print('I am %s years old.' % age)

print('My name is %s. I am %i years old' % (name, age))
print('My name is %(first_name)s. I am %(my_age)i years old.' %
      {'first_name': name, 'my_age': age})

# using .format
print();
age = 21
name = 'Jude'
print('My name is {} and I am {} years old.'.format(name, age))

# In Python when you see a double asterisk (**) used like this, it means that you are passing named parameters to the function. So Python is converting the dictionary to first_name=name, age=age for you.
print('My name is {first_name} and I am {age} years old.'.format(
  **{'first_name':name, 'age':age}))

# String width and alignment
left_aligned = '{:<20}'.format('left aligned')
print(f'"{left_aligned}"')

