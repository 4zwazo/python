def count():
  n = 0
  while True:
    n += 1
    yield n

counter = count()
print(counter)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))