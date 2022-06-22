alist = [1, 2, 3, 12, 8, 4, 32, 53, 31, 87, 65]
blist = []
n = int(input("enter number: "))
for i in alist:
  if i <= n:
    blist.append(i)
print(*blist)