class Person():
	__first: str
	__last: str
	__pay: int

	def __init__(self, first: str, last: str, pay: int) -> None:
		self.__first = first
		self.__last = last
		self.__pay = pay

	def get_first(self):
		return self.__first
	
	def get_last(self):
		return self.__last

	def get_pay(self):
		return self.__pay

	def __info(self):
		print(f'{self.__first} {self.__name} {self.__pay}')
	
	def display(self):
		self.__info()

obj1 = Person('Jude', 'Pierre', 9000)
print(obj1.get_pay())

