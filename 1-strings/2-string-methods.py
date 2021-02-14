# In python everything is an object
# Strings have methods you can call on them

name = 'pascal laurent'
name.capitalize()

print(name.capitalize()) #=> Pascal laurent
print(name.title()) #=> Pascal laurent
print(name.upper()) #=> PASCAL LAURENT
print(name.lower()) #=> pascal laurent

print(dir(name)) # listing of methods and attributes you can call on strings

# remove space from around the string
name = '      Pascal     '
print(f'|{name}|')
print(f'|{name.strip()}|')

# cut the string into separate words, produces a list of words
text = 'This.is.so.cool.to.learn.Python'
print(text.split())

# give the 2nd word in the list
print(text.split()[0])

# ['This', 'is.so.cool.to.learn.Python']
print(text.split('.', 1))

# ['This', 'is', 'so.cool.to.learn.Python']
print(text.split('.', 2))

