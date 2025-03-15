class Student:
    def __init__(self, num, height, weight):
        self.num = num
        self.height = height
        self.weight = weight

n = int(input())
student_list = []
for i in range(n):
    height, weight = map(int, input().split())
    student_list.append(Student(i+1, height, weight))
student_list.sort(key= lambda x: (x.height, -x.weight))
for student in student_list:
    print(student.height, student.weight, student.num)