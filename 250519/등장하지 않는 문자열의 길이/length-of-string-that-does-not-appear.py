n = int(input())
s = input()
for length in range(1, n):
    chk = 0
    for i in range(len(s)-length+1):
        if s.count(s[i:i+length]) >= 2:
            chk = 1
    if chk == 0:
        ans = length
        break
print(ans)