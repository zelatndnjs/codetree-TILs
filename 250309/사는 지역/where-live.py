n = int(input())
class Person:
    def __init__(self, name='a', adress='a', region='a'):
        self.name = name
        self.adress = adress
        self.region = region

people = [Person() for i in range(n)]
for i in range(n):
    a,b,c = input().split()
    people[i].name = a
    people[i].adress = b
    people[i].region = c

people.sort(key=lambda p: p.name, reverse=True)
print(f"name {people[0].name}")
print(f"addr {people[0].adress}")
print(f"city {people[0].region}")
