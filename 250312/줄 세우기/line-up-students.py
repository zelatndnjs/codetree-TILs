class Student:
    def __init__(self, height, weight, number):
        self.height = int(height)
        self.weight = int(weight)
        self.number = int(number)

n = int(input())
data = [tuple(map(int, input().split())) + (i+1,) for i in range(n)]
students = [Student(height, weight, number) for height, weight, number in data]
students.sort(key=lambda x: (-x.height, -x.weight, x.number))
for student in students:
    print(student.height, student.weight, student.number)