n = int(input())
num = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i,n):
        if sum(num[i:j+1])/len(num[i:j+1]) in num[i:j+1]:
            # print(f"시작점: {num[i]}, 끝점: {num[j]}, 평균: {sum(num[i:j+1])/len(num[i:j+1])}")
            cnt += 1
print(cnt)