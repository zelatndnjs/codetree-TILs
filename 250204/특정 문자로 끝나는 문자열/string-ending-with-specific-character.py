a = list()
for i in range(10):
    b = input()
    a.append(b)
c = input()
cnt = 0
for i in a:
    if i[-1] == c:
        print(i)
        cnt += 1
if cnt==0:
    print("None")