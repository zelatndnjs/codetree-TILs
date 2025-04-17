n = int(input())
s = input()
cnt = 0
for i in range(len(s)-2):
    if s[i] == 'C':
        for j in range(i+1, len(s)-1):
            if s[j] == 'O':
                for k in range(j+1, len(s)):
                    if s[k] == 'W':
                        cnt += 1
print(cnt)