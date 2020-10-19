# False maps to 0 and True maps to 1

print(True == 1)
print(False == 0)

# bool() function to cast other type to True or False
print(bool('2'))    #=> True
print(bool('bool')) #=> True

print(bool({1: 'peter'})) #=> True
print(bool(1))    #=> True

print(bool(0.00)) #=> False
print(bool(0)) #=> False

print(bool('')) #=> False
print(bool([])) #=> False
print(bool({})) #=> False
