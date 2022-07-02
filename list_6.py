def useless_list(input_list):
  return max(input_list) / len(input_list)
y = 'y'
while y == 'y':
  input_list = input('enter list of elements, using comma: ').split(',')
  float_input_list = list(map(float, input_list))
  print(useless_list(float_input_list))
  y = input('restart?(y/n): ')
  