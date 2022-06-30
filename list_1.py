y = 'y'
while y == 'y':
  input_data = input("Enter list of numbers, using comma: ").split(',')
  int_input_data = map(int, input_data)
  alist = list(int_input_data)
  blist = []
  n = int(input("enter number: "))
  for i in alist:
    if i <= n:
      blist.append(i)
  print(*blist)
  y = input("restart?(y/n): ", )
