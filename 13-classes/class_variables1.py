class Person():
	inc_factor = 1.3

	def __init__(self, first_name, last_name, pay):
		self.first_name = first_name
		self.last_name = last_name
		self.pay = pay

	def getFullName(self):
		return f'{self.first_name} {self.last_name}'
	
	def email(self):
		return self.getFullName().replace(' ','')+'@gmail.com'

	def increment_pay(self):
		self.pay = self.pay*Person.inc_factor


# Instance variables
obj1 = Person('Jude', 'Pierre', 90000)
obj2 = Person('Mamie', 'Etienne', 80000)

print(obj1.pay)
obj1.increment_pay()
print(obj1.pay)
