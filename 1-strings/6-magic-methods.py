name = "jude 124 lakay"

name1 = name.__add__(" nou")
name2 = name + "nou"
print(name1)
print(name2)

is_text  = name.__contains__("124")
is_text2 = "124" in name
print(is_text)
print(is_text2)

name = "pas"
print(name.__eq__("pas"))
print(name == "pas")

letter_position  = name.__getitem__(2)
letter_position1 = name[2]
print(letter_position)
print(letter_position1)