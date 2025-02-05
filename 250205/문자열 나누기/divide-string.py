n = int(input())
num = input().split()
result = "".join(num)
for i in range(len(result)):
    if i%5==0 and i != 0:
        print()
    print(result[i],end="")