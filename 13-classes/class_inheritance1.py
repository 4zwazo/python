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

class Trainer(Person):
	def __init__(self, first_name, last_name, pay, subject='NoSubject'):
		Person.__init__(self, first_name, last_name, pay)
		self.subject = subject

	def Subject(self):
		return f'{self.getFullName()} is teaching {self.subject}'

class Manager(Trainer):
	def __init__(self, first_name, last_name, pay, dep):
		super().__init__(first_name, last_name, pay)
		self.dep = dep

	def department(self):
		return f'{self.getFullName()} is manager in {self.dep}'

class Assistant_Manager(Manager):
	def __init__(self, first_name, last_name, pay, dep, sub_dep):
		super().__init__(first_name, last_name, pay, dep)
		self.sub_dep = sub_dep
	
	def sub_department(self):
		return f'{self.getFullName()} is manager in {self.sub_dep}'


# Instance variables
obj0 = Person('Pascal', 'George', 4000)
obj1 = Trainer('Jude', 'Pierre', 90000, 'math')
obj2 = Manager('Mamie', 'Juste', 17000, 'Computer')
obj3 = Assistant_Manager('John', 'Doe', 2000, 'Statistic', 'Cloud')

print(obj0.getFullName())

print(obj1.getFullName())
print(obj1.Subject())

print(obj2.getFullName())

print(obj3.getFullName())
print(obj3.department())
print(obj3.sub_department())
print(Assistant_Manager.__mro__)


