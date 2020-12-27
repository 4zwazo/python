items = [[0, 'a', 2], [5, 'b', 0], [2, 'c', 1]]

# sort the list base on the position of the 2nd item in the list_words
def second(item):
  return item[1]

sorted_list = sorted(items, key=second)
print(sorted_list)

# using lambda

sorted_list = sorted(items, key=lambda item: item[1])
print(sorted_list)

sorted_list = sorted(items, key=lambda item: item[0])
print(sorted_list)

sorted_list = sorted(items, key=lambda item: item[2])
print(sorted_list)