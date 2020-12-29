def fib():
  first = 0
  last = 1
  while True:
    first, last = last, first + last
    # first, last =   1,  (0    +   1) => first = 1, last = 1
    # first, last =   1,  (1    +   1) => first = 1, last = 2
    # first, last =   2,  (1    +   2) => first = 2, last = 3
    # first, last =   3,  (2    +   3) => first = 3, last = 5
    # first, last =   5,  (3    +   5) => first = 3, last = 5

    yield first
    # first = 1
    # first = 1
    # first = 2
    # first = 3
    # first = 5

f = fib()
print(next(f)) #=> 1
print(next(f)) #=> 1
print(next(f)) #=> 2
print(next(f)) #=> 3
print(next(f)) #=> 5

print("\n")

# iterate using the generator
f = fib()
for x in f:
  print(x)
  if x > 20:
    break