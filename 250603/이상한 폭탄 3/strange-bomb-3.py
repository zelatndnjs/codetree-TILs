n,k = map(int, input().split())
bomb = [int(input()) for _ in range(n)]
bombdic = dict()
for i in range(n):
    for j in range(max(0,i-k), min(n,i+k)):
        if i != j and bomb[i] == bomb[j]:
            if bomb[i] in bombdic:
                bombdic[bomb[i]] += 1
            else:
                bombdic[bomb[i]] = 1
            break
a=sorted(bombdic.items(), key=lambda x:x[1], reverse=True)
if len(a) == 0:
    print(0)
else:
    print(a[0][0])