def useless_list(input_list):
  return round(max(input_list) / len(input_list, 4)
y = 'y'
while y == 'y':
  input_list = input('enter list of float elements, using comma: ').split(',')
  float_input_list = list(map(float, input_list))
  print(useless_list(float_input_list))
  y = input('restart?(y/n): ')
  
