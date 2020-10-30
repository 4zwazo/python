# To turn the regular method into the class method, 
# we would use a decorator (@classmethod) at the top of the method
#
class Person():
	inc_factor = 1.3

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

	def email(self):
		return f'{self.first}@gmail.com'
	
	def increment(self):
		self.pay = self.pay*Person.inc_factor
		return self.pay
	
	@classmethod
	def inc_change(cls, amount):
		cls.inc_change = amount
	
	@classmethod
	def prep_constructor(cls, str1):
		first, last, pay = str1.split()
		return cls(first, last, int(pay))

obj1 = Person('Jude', 'Pierre', 9000)
obj2 = Person.prep_constructor('Pascal Juste 45678')

print(obj1.increment())
Person.inc_change(1.5)
print(obj1.increment())
print(obj2.increment())


