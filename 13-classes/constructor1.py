class Person():
	def __init__(self, first_name, last_name, pay):
		self.first_name = first_name
		self.last_name = last_name
		self.pay = pay

	def getFullName(self):
		return f'{self.first_name} {self.last_name}'
	
	def email(self):
		return self.getFullName().replace(' ','')+'@gmail.com'

# Instance variables
obj1 = Person('Jude', 'Pierre', '90000')
obj2 = Person('Mamie', 'Etienne', '80000')

print(f'Full Name: {obj1.first_name} {obj1.last_name}')
print(f'Full Name: {obj2.first_name} {obj2.last_name}')

print(obj1.getFullName())
print(obj2.getFullName())

print(obj1.email())
print(obj2.email())