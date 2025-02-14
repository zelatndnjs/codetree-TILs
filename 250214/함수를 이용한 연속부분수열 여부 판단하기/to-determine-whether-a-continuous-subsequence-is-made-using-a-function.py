n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt = 0
chk = 0
for i in range(len(a)-len(b)+1):
    cnt = 0
    for j in range(len(b)):
        if a[i+j] == b[j]:
            cnt += 1
            if cnt == len(b):
                chk = 1
                print("Yes")
                break
        else:
            continue
if chk == 0:
    print("No")