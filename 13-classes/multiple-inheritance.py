class A():
	def sum1(sekf, a, b):
		return a + b

class B():
	def mul(self, a, b):
		return a*b

class C(A, B):
	pass

obj1 = C()
print(obj1.sum1(10, 20))
print(obj1.mul(10, 20))