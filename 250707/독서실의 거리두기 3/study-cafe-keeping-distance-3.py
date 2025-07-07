n = int(input())
seats = input()
position = []
for i in range(n):
    if seats[i] == '1':
        position.append(i)
distance = []
for i in range(len(position)-1):
    distance.append(position[i+1] - position[i])
distance.append(max(distance)//2)
distance.append(max(distance) - max(distance)//2)
m=max(distance)
distance.remove(m)
print(min(distance))