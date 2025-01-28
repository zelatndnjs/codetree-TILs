n = int(input())
num = list(map(int, input().split()))
new = sorted(num, reverse=True)
print(new[0], new[1])
