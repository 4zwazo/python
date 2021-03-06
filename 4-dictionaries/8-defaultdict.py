from collections import defaultdict

# With defaultdict you can access or modify keys that don’t exist in the dictionary.
#
scores_done = [('jude', 90), ('paul', 45), ('martin', 67),
               ('jude', 10), ('paul', 55), ('martin', 77)]
challenges = {}

# if try to access in challenges you get keyerror
# for name, score in scores_done:
#     challenges[name].append(score)

# here it comes defaultdict
challenges = defaultdict(list)

for name, score in scores_done:
     challenges[name].append(score)

print(challenges)