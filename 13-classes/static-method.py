class Person():
	inc_factor = 1.3

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

	def email(self):
		return f'{self.first}@gmail.com'
	
	def increment(self):
		if self.decide(self.pay):
			return self.pay*Person.inc_factor
		else:
			return self.pay
	
	@staticmethod
	def decide(pay):
		if pay <= 5000:
			return True
		else:
			return False

obj1 = Person('Jude', 'Pierre', 9000)
obj2 = Person('Pascal', 'Juste', 3000)

print(obj1.increment())
print(obj2.increment())

