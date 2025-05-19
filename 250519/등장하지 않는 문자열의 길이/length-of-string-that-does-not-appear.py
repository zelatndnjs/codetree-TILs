n = int(input())
s = input()
for length in range(1, n):
    chk = 0
    word = []
    for i in range(n-length+1):
        word.append(s[i:i+length])
    for i in range(len(word)-1):
        for j in range(i+1,len(word)):
            if word[i] == word[j]:
                chk = 1
                break
    if chk == 0:
        ans = length
        break
print(ans)