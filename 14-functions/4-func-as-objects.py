def double(input):
  ''' Double input'''
  return input * 2

def triple(input):
  ''' Triple input '''
  return input * 3

functions = [double, triple]

for function in functions:
  print(double(3))