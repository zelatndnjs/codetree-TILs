n = int(input())
a = list(input().split())
ans = 0
for i in range(n):
    target = chr(i+65)
    ans += a.index(target) - i
    # print("수정 전")
    # print(a)
    a.remove(target)
    a.insert(i, target)
    # print("수정 후")
    # print(a)
print(ans)