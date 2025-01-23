n = int(input())
num = n
for i in range(1,n+1):
    for j in range(1, num+1):
        if j != num:
            print(f"{i} * {j} = {i*j}", end=' / ')
        else:
            print(f"{i} * {j} = {i * j}")
    num -= 1