n = int(input())
num = list(map(int, input().split()))
if n == 3:
    print(num[0] * num[1] * num[2])
else:
    ans = []
    plus = []
    minus = []
    zero = []
    for i in num:
        if i < 0 :
            minus.append(i)
        elif i > 0:
            plus.append(i)
        else:
            zero.append(i)
    plus.sort()
    minus.sort()
# 경우의 수 : plus 3개, plus 1개 minus 2개, 0, plus 2개 minus 1개, minus 3개
    if len(plus) >= 3:
        ans.append(plus[-1] * plus[-2] * plus[-3])
    if len(plus) >= 1 and len(minus) >= 2:
        ans.append(minus[0] * minus[1] * plus[-1])
    if len(zero) >= 1:
        ans.append(0)
    if len(plus) >= 2 and len(minus) >= 1:
        ans.append(plus[0] * plus[1] * minus[-1])
    if len(minus) >= 3:
        ans.append(minus[-1] * minus[-2] * minus[-3])
    print(max(ans))