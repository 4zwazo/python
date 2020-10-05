# Review Questions
# ----------------
# 1. How do you create a list?
my_list = [1, 2, 3]
another_list = []
yet_another_list = list()

# 2. Create a list with 3 items and then use append() to add two more.
my_list = ['papa', 'mama', 'tati']
my_list.append('sis')
my_list.append('aunti')

# 3. What is wrong with this code?
# >>>my_list=[1,2,3]
# >>>my_list.remove(4)
# item 4 is not in my_list

# 4. How do you remove the 2nd item in this list?
my_list=[1,2,3]
my_list.pop(1)
print(my_list)

# 5. Create a list that looks like this: [4, 10, 2, 1, 23]. Use string slicing to get only the middle 3 items.
list_numbers = [4, 10, 2, 1, 23]
middle_number = list_numbers[2:3]
print(middle_number)