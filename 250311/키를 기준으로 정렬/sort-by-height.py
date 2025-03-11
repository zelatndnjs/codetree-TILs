class Score:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
data = [tuple(input().split()) for _ in range(n)]
students = [Score(name, kor, eng, math) for name, kor, eng, math in data]
students.sort(key=lambda x: (x.kor, x.eng, x.math), reverse=True)
for student in students:
    print(student.name, student.kor, student.eng, student.math)