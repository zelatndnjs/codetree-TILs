class Score:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = int(kor)
        self.eng = int(eng)
        self.math = int(math)

n = int(input())
data = [tuple(input().split()) for _ in range(n)]
students = [Score(name, kor, eng, math) for name, kor, eng, math in data]
students.sort(key=lambda x: x.kor+x.eng+x.math)
for student in students:
    print(student.name, student.kor, student.eng, student.math)