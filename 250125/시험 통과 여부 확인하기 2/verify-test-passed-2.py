n = int(input())
cnt=0
for _ in range(n):
    a,b,c,d = map(int,input().split())
    if (a+b+c+d)/4 >= 60:
        print("pass")
        cnt+=1
    else:
        print("fail")
print(cnt)