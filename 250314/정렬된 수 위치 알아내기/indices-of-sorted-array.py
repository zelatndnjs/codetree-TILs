class Number:
    def __init__(self,num, firstplace=0, sortplace=0):
        self.num = num
        self.firstplace = firstplace
        self.sortplace = sortplace

n = int(input())
data = tuple(map(int, input().split()))
numbers = []
for i in range(n):
    numbers.append(Number(data[i], i+1))

numbers.sort(key=lambda x: x.num)
for i in range(n):
    numbers[i].sortplace = i+1

numbers.sort(key=lambda x: x.firstplace)
for i in numbers:
    print(i.sortplace, end=' ')