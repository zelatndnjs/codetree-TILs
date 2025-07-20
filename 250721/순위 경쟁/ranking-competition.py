n = int(input())
ascore = 0
bscore = 0
cscore = 0
scores = [0,0,0] # a,b,c
best = 'none'
ans = 0
for i in range(n):
    name, score = input().split()
    score = int(score)
    if name == 'A':
        scores[0] += score
    elif name == 'B':
        scores[1] += score
    else:
        scores[2] += score
    big = max(scores)
    newbest = ''
    if scores[0] == big:
        newbest += 'A'
    if scores[1] == big:
        newbest += 'B'
    if scores[2] == big:
        newbest += 'C'
    if best != newbest:
        ans += 1
        best= newbest
print(ans)
