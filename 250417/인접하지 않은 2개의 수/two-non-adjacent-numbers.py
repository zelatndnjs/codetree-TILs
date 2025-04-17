import sys
m = -sys.maxsize
n = int(input())
num = list(map(int, input().split()))
for i in range(len(num)-2):
    for j in range(i+2, len(num)):
        if num[i]+num[j] > m:
            m = num[i]+num[j]
print(m)