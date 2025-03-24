n,m,k = map(int,input().split())
students = [0 for i in range(n+1)]
result = [-1]
for i in range(m):
    num = int(input())
    students[num] += 1
    if students[num] >= k:
        if len(result) == 1:
            result.append(num)
print(result[-1])