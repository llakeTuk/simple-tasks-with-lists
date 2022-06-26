origin_string = input('enter string: ')
list_string = [origin_string[0]]
list_count = [0]
for i in origin_string:
  if list_string.count(i) == 0:
    list_string.append(i)
    list_count.append(1)
  else:
    j = list_string.index(i)
    list_count[j] += 1
print(*list_string)
print(*list_count) "update to print in one row(a: 1, b: 2)"
