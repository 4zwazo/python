# Write a list comprehension that results in a list of every letter in the word smogtether capitalized.

letter = "smogtether"
letter_list = [x.upper() for x in letter]
print(letter_list)