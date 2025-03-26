N, K, P, T = map(int, input().split())
# N = 총 개발자 수
# K = K번의 악수 동안 전염병 옮김
# P = 처음 전염병에 걸려있는 개발자 번호
# T = 악수의 횟수
handshakes = [tuple(map(int, input().split())) for _ in range(T)]  # t, x, y = t초에 x 개발자와 y개발자가 악수 나눔


class Developer:
    def __init__(self, sick=0, lefthandshake=0, num=0):
        self.sick = sick
        self.lefthandshake = lefthandshake
        self.num = num


developers = [Developer(0, 0, i) for i in range(1, N + 1)]
developers[P - 1].sick = 1
developers[P - 1].lefthandshake = K
handshakes.sort(key= lambda x: x[0])
for t, x, y in handshakes:
    # print(f"{x}번 개발자와 {y}번 개발자가 만남!")
    # print(f"{x}번 개발자의 정보는")
    # print(f"아프면 1 안 아프면 0 : {developers[x - 1].sick}")
    # print(f"남은 악수 횟수 : {developers[x - 1].lefthandshake}")
    # print(f"{y}번 개발자의 정보는")
    # print(f"아프면 1 안 아프면 0 : {developers[y - 1].sick}")
    # print(f"남은 악수 횟수 : {developers[y - 1].lefthandshake}")
    if developers[x - 1].lefthandshake > 0 and developers[y - 1].sick == 0:
        developers[x - 1].lefthandshake -= 1
        developers[y - 1].sick = 1
        developers[y - 1].lefthandshake = K
    elif developers[y - 1].lefthandshake > 0 and developers[x - 1].sick == 0:
        developers[y - 1].lefthandshake -= 1
        developers[x - 1].sick = 1
        developers[x - 1].lefthandshake = K
    else:
        continue
    # print("만난 후!")
    # print(f"{x}번 개발자의 정보는")
    # print(f"아프면 1 안 아프면 0 : {developers[x - 1].sick}")
    # print(f"남은 악수 횟수 : {developers[x - 1].lefthandshake}")
    # print(f"{y}번 개발자의 정보는")
    # print(f"아프면 1 안 아프면 0 : {developers[y - 1].sick}")
    # print(f"남은 악수 횟수 : {developers[y - 1].lefthandshake}")
for i in developers:
    print(i.sick, end='')
