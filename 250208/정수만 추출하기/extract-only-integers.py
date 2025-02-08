a,b = input().split()
A = ""
B = ""
for i in a:
    if i.isdigit():
      A += i
    else:
        break

for i in b:
    if i.isdigit():
      B += i
    else:
        break
A = int(A)
B = int(B)
print(A+B)
