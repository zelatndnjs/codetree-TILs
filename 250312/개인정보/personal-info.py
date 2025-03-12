class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = int(height)
        self.weight = float(weight)


data = [tuple(input().split()) for _ in range(5)]
students = [Student(name, height, weight) for name, height, weight in data]
students.sort(key=lambda student: student.name)
print("name")
for i in students:
    print(i.name, i.height, i.weight)

print()
students.sort(key=lambda student: -student.height)
print("height")
for i in students:
    print(i.name, i.height, i.weight)