# notice that parentheses used when creating the generator
list_numbers = (x for x in range(5))
print(list_numbers)

print(next(list_numbers))
print(next(list_numbers))
print(next(list_numbers))
print(next(list_numbers))
print(next(list_numbers))
# print(next(list_numbers))

# creating a list
list_numbers_2 = [x for x in range(5)]
print(list_numbers_2)

# Memory usage between list_numbers and list_numbers_2
import sys

print(f'list_of_numbers used {sys.getsizeof(list_numbers)} bytes')
print(f'list_of_numbers_2 used {sys.getsizeof(list_numbers_2)} bytes')