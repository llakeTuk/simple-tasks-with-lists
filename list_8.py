def all_equal(input_list):
  max_item = max(input_list, key = lambda x: len(x))
  max_len = len(max_item)
  return [i.ljust(max_len, '_') for i in input_list]
y = 'y'
while y == 'y':
  input_list = input('enter list of elements, using comma: ').split(',')
  print(*all_equal(input_list))
  y = input('restart?(y/n): ')
print('goodbye')