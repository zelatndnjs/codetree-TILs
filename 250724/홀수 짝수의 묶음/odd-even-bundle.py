n = int(input())
num = list(map(int ,input().split()))
evens = []
odds = []
for i in num:
    if i % 2==0:
        evens.append(i)
    else:
        odds.append(i)
a = len(evens)
b = len(odds)
ans = 0
chk = 0 # 0이면 짝수 쌓기 1이면 홀수 쌓기
while True:
    if len(evens) == 0 and len(odds) == 0:
        break
    if chk ==0:
        if len(evens)>=1:
            ans += 1
            evens.pop()
            chk = 1
            a = len(evens)
        else:
            if len(odds) >= 2:
                ans += 1
                odds.pop()
                odds.pop()
                chk = 1
                b = len(odds)
            else:
                ans -= 1
                break
    else:
        if len(odds) >= 1:
            ans += 1
            odds.pop()
            chk = 0
            b = len(odds)
        else:
            break
print(ans)