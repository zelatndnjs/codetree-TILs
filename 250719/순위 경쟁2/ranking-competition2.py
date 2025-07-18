n = int(input())
ascore = 0
bscore = 0
numberone = 'none'
change = 0
for i in range(n):
    name, score = input().split()
    score = int(score)
    if name == 'A':
        ascore += score
    else:
        bscore += score
    if numberone == 'A':
        if ascore == bscore:
            change += 1
            numberone = 'AB'
        elif ascore < bscore:
            change += 1
            numberone = 'B'
    elif numberone == 'B':
        if ascore == bscore:
            change += 1
            numberone = 'AB'
        elif ascore > bscore:
            change += 1
            numberone = 'A'
    else:
        if ascore > bscore:
            change += 1
            numberone = 'A'
        elif ascore < bscore:
            change += 1
            numberone = 'B'
print(change)
