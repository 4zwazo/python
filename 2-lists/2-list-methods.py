"""
append()
clear()
copy()
count()
extend()
index()
insert()
pop()
remove()
reverse()
sort()
"""

# count()
list_numbers = [1, 4, 1, 6]
print(list_numbers.count(1))

# reverse()
list_number_reverse = list_numbers.reverse();
print(list_number_reverse) # because the reserve is in place
print(list_numbers)

# append()
list_words = ['house', 'cake', 'peanut']
list_words.append('car')
print(list_words)

# extend()
list_fruits = ['apple', 'grapes']
list_words.extend(list_fruits)
print(list_words)

# insert()
list_words.insert(0, 'marbles')
print(list_words)

# Delete items from a list

# remove()
list_words.remove('cake')
print(f'The new list: {list_words}')

# pop()
word_removed = list_words.pop()
print(f'{word_removed} is removed. The new list: {list_words}')

word_removed = list_words.pop(3)
print(f'{word_removed} is removed. The new list: {list_words}')

list_words.clear()

# Sorted a List

# sort()
list2_words = ['papa', "mama", 'tati', 'yomo']
list2_words.sort()
print(list2_words)

list2_words.append('beets')
sorted_list = sorted(list2_words)
print(sorted_list)

reserse_sort = sorted(list2_words, reverse=True)
print(reserse_sort)




