# In python everything is an object
# Strings have methods you can call on them

name = 'pascal'
name.capitalize()

print(name.capitalize()) #=> Pascal
print(name.upper()) #=> PASCAL
print(name.lower()) #=> pascal

print(dir(name)) # listing of methods and attributes you can call on strings

# remove space from around the string
name = '      Pascal     '
print(f'|{name}|')
print(f'|{name.strip()}|')

# cut the string into separate words, produces a list of words
text = 'This is so cool to learn Python'
print(text.split())

# give the 2nd word in the list
print(text.split()[1])

