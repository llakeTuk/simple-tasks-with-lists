def change_list(input_list):
  new_first = input_list.pop()
  new_last = input_list.pop(0)
  input_list.insert(0, new_first)
  input_list.append(new_last)
  return input_list
y = 'y'
while y == 'y':
  input_list = input('enter list of elements, using comma: ').split(',')
  print(*change_list(input_list))
  y = input('restart?(y/n): ')
  