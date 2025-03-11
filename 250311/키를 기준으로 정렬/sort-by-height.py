class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
n = int(input())
data = [tuple(input().split()) for _ in range(n)]
people = [Person(name, height, weight) for name, height, weight in data]
people.sort(key = lambda p: p.height)
for person in people:
    print(person.name, person.height, person.weight)