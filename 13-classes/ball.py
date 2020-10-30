'''
Everything in Python is an object. What that means is that everything you create in Python has functions or attributes or both attached to them that you can use.

A class has
- attributes
- actions
'''
# Creating a class Ball with 3 attributes
class Ball:
	def __init__(self, color: str, size: int, weight: int, ball_type: str) -> None:
		self.color = color
		self.size = size
		self.weight = weight
		self.ball_type = ball_type

	def bounce(self):
		if self.ball_type.lower() == 'bowling':
			print('Bowling ball can not bounce')
		else:
			print(f'The {self.ball_type} ball is bouncing')

	def __repr__(self) -> str:
		return f'<Ball: {self.color} {self.ball_type}>'

if __name__ == '__main__':
	print(__name__)
	# Create instances of the class Ball
	ball_one = Ball('red', 15, 1, 'beach')
	ball_two = Ball('black', 12, 3, 'bowling')
	
	ball_one.bounce()
	ball_two.bounce()