y = 'y'
while y == 'y':
  input_data = input('enter list of numbers, using comma: ').split(',')
  input_list = map(int, input_data)
  alist = list(input_list)
  print(alist)
  alist.reverse()
  print(alist)
  y = input('restart?(y/n): ')