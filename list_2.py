y = 'y'
while y == 'y':
  input_data_alist = input("Enter A-list of numbers, using comma: ")
  input_data_blist = input("Enter B-list of numbers, using comma: ")
  splited_input_data_a = input_data_alist.split(',')
  splited_input_data_b = input_data_blist.split(',')
  int_input_data_a = map(int, splited_input_data_a)
  int_input_data_b = map(int, splited_input_data_b)
  alist = list(int_input_data_a)
  blist = list(int_input_data_b
  clist = []
  for i in alist:
    if blist.count(i) != 0:
      clist.append(i)
  print(*clist)
  y = input("restart?(y/n): ")
