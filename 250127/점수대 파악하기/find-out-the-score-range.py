cnt = [0 for i in range(11)]
scores = list(map(int, input().split()))
for i in scores:
    if i==0:
        break
    cnt[i//10] += 1

for i in range(10,0,-1):
    print(i*10,'-',cnt[i])