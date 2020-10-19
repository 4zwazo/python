# None is a NoneType
# None is python's null value

print(None == 0) #=> False
print(None == 1) #=> False
print(None == '') #=> False
print(None == None) #=> True

# all instance of None points to the same object
a = None
b = None

print(f'{id(a)} = {id(b)}')

# Great way to check if a variable is None use the is operator
# is will check the variable’s identity and verify that it really is None
if (a is None):
  print('Yes I am None')