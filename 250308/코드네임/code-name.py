class Agent:
    def __init__(self, codename='a', score=0):
        self.codename = codename
        self.score = score

agents = [Agent() for _ in range(5)]

for i in agents:
    a,b = input().split()
    b = int(b)
    i.codename = a
    i.score = b

min = agents[0].score

for i in agents:
    if i.score < min:
        min = i.score

for i in agents:
    if i.score == min:
        print(i.codename, i.score)
