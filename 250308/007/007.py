class Spy:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

    def printSpy(self):
        print(f"secret code : {secret_code}")
        print(f"meeting point : {meeting_point}")
        print(f"time : {time}")


secret_code, meeting_point, time = input().split()
time = int(time)

Spy1 = Spy(secret_code, meeting_point, time)
Spy1.printSpy()