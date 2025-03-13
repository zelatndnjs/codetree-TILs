class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
people = []
for i in range(n):
    name, height, weight = input().split()
    people.append(Person(name, int(height), int(weight)))
people.sort(key=lambda x: (x.height, -x.weight))
for person in people:
    print(person.name, person.height, person.weight)