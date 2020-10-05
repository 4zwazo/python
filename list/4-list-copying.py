# copy() create a shallow copy of the object
list_words = ['house', 'cake', 'peanut', 'car', 'tv', 'computer']
list2_words = list_words.copy()
print(list_words)
print(list2_words)

list2_words.append('monitor')
print(list2_words)


# impact of shallow copy
list_numbers = [1,2,3,['a', 'd', 'c'], 7, 9]
new_number_list = list_numbers.copy()
print(list_numbers)
print(new_number_list)

new_number_list[3][1] = 'b'
print()
print(list_numbers)
print(new_number_list)

# another way to copy
new_list = list_numbers[:]
print(new_list)

new_list[3][2] = 'a'
print()
print(list_numbers)
print(new_list)


# yet another way
new_list_2 = list(new_list)
new_list_2[3].append('c')
print()
print(new_list)
print(new_list_2)
