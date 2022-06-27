y = 'y'
While y == 'y':
  input_data = input("Enter list of numbers, using comma: ")
  splited_input_data = input_data.split(',')
  int_input_data = map(int, splited_input_data)
  alist = list(int_input_data)
  blist = []
  n = int(input("enter number: "))
  for i in alist:
    if i <= n:
      blist.append(i)
  print(*blist)
  y = input("restart?(y/n): ", )
