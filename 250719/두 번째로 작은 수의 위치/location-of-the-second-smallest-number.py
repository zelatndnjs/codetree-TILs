n = int(input())
num = list(map(int, input().split()))
setnum = sorted(set(num))
if len(setnum) == 1:
    print(-1)
elif num.count(setnum[1]) >= 2:
    print(-1)
else:
    print(num.index(setnum[1])+1)