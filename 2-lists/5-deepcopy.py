from copy import deepcopy

list_numbers = [1,2,3,['a', 'd', 'c'], 7, 9]
new_number_list = deepcopy(list_numbers)
print(list_numbers)
print(new_number_list)

print()
new_number_list[3][1] = 'ba'
print(list_numbers)
print(new_number_list)
