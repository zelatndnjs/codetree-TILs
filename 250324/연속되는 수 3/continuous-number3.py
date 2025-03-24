n = int(input())
num = [] # 2 7 7 7 7 5 7
for i in range(n):
    num.append(int(input()))
cnt = []
a = 1
if n == 1:
    print(1)
else:
    for i in range(1, n):
        if num[i] * num[i-1] >0:
            a+= 1
        else:
            cnt.append(a)
            a = 1
    cnt.append(a)
    print(max(cnt))
