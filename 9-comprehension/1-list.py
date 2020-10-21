numbers = [1,2,3,4,5,6,7,8,9,10]
new_list = []

for x in numbers:
  new_list.append(x)
print(new_list)

# using list comprehension
new_list = [x for x in numbers]
print(new_list)

# double each number
new_list = [x*2 for x in numbers]
print(new_list)

# filter the list
new_list = [x*2 for x in numbers if x%2]
print(new_list)

# nested for loop
my_dict={1:'dog',2:'cat',3:'python'}
new_dict = [(num,animal) for num in my_dict for animal in my_dict.values() \
  if my_dict[num] == animal]
print(new_dict)

for key, val in new_dict:
  print(f'{key}:{val}')