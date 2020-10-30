class Person:
	pass

obj1 = Person()
obj2 = Person()

# Instance variables
obj1.first_name = 'Jude'
obj1.last_name = 'Pierre'
obj1.pay = '90000'

# Instance variables
obj2.first_name = 'Mamie'
obj2.last_name = 'Etienne'
obj2.pay = '80000'

print(f'Full Name: {obj1.first_name} {obj1.last_name}')
print(f'Full Name: {obj2.first_name} {obj2.last_name}')