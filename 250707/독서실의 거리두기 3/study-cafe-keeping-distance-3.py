n = int(input())
seats = input()
position = []
for i in range(n):
    if seats[i] == '1':
        position.append(i)
distance = []
for i in range(len(position)-1):
    distance.append(position[i+1] - position[i])
print(max(distance)//2)