num  = (1).__add__(5)
num2 = int.__add__(4, 4)
print(num)
print(num2) 

text = 'Jude'.__add__(' Pierre')
text1 = str.__add__('Jude', ' Pierre')
print(text)
print(text1)

class Person():
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

	def email(self):
		return f'{self.first}@gmail.com'
	
	def __add__(self, other):
		return self.pay + other.pay

	def __gt__(self, other):
		return self.pay > other.pay

obj1 = Person('Jude', 'Pierre', 9000)
obj2 = Person('Mamie', 'Jean', 6000)

print(obj1 + obj2) #=> obj1.__add__(obj2)
print(obj1 > obj2) #=> obj1.__gt__(obj2)

