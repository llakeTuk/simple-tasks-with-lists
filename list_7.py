def sort_list(input_list):
  input_list.sort(key = lambda x: abs(x), reverse = True)
  return input_list
y = 'y'
while y == 'y':
  input_list = input('enter list of elements, using comma: ').split(',')
  float_input_list = list(map(float, input_list))
  print(sort_list(float_input_list))
  y = input('restart?(y/n): ')
  