N = int(input())
num = list(map(int, input().split()))
print(min(num), num.count(min(num)))