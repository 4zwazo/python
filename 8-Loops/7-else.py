numbers = [1,2,3,4,5,6,7,8,9,10,11,8,13,14]
for num in numbers:
  if num == 19:
    print('found number 8')
    break
  print(num)
else:
  print('number 8 not found')