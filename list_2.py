y = 'y'
while y == 'y':
  input_data_alist = input("Enter A-list of numbers, using comma: ").split(',')
  input_data_blist = input("Enter B-list of numbers, using comma: ").split(',')
  int_input_data_a = map(int, input_data_alist)
  int_input_data_b = map(int, input_data_blist)
  alist = list(int_input_data_a)
  blist = list(int_input_data_b)
  clist = []
  for i in alist:
    if blist.count(i) != 0:
      clist.append(i)
  print(*clist)
  y = input("restart?(y/n): ")
