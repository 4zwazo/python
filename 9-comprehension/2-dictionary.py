my_dict= ['dog', 'cat', 'python']
my_dict_index = [3, 4, 5]

new_dict = {my_dict_index[key]:value for key, value in enumerate(my_dict)}
print(new_dict)

# when you create a dictionary comprehension as the keys have to be hashable