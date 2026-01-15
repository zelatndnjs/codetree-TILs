# 뱀 게임 시뮬레이션 (deque + set)
# 입력 형식 (예시):
# N M K
# (사과 M개) x y
# (명령 K개) D p   (D는 U/D/L/R, p는 초)
#
# 출력: 게임 종료까지 걸린 시간(초)

from collections import deque

def main():
    n, m, k = map(int, input().split())

    grid = [[0] * n for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        grid[x - 1][y - 1] = 1

    commands = []
    for _ in range(k):
        direction, seconds = input().split()
        commands.append((direction, int(seconds)))

    direction_to_delta = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1),
    }

    snake_body = deque([(0, 0)])     # 머리 -> 꼬리
    snake_cells = set([(0, 0)])      # 점유 칸 (충돌 O(1) 확인)

    elapsed_seconds = 0

    for direction, seconds_to_move in commands:
        dx, dy = direction_to_delta[direction]

        for _ in range(seconds_to_move):
            head_x, head_y = snake_body[0]
            next_x, next_y = head_x + dx, head_y + dy

            # 1) 벽 충돌
            if not (0 <= next_x < n and 0 <= next_y < n):
                print(elapsed_seconds + 1)
                return

            has_apple = (grid[next_x][next_y] == 1)

            # 2) 사과가 없으면 "꼬리를 먼저" 제거해서 공간을 비워준다
            if not has_apple:
                tail_x, tail_y = snake_body.pop()
                snake_cells.remove((tail_x, tail_y))

            # 3) 이제 몸 충돌 체크 (꼬리 칸으로 들어가는 경우도 자연스럽게 처리됨)
            if (next_x, next_y) in snake_cells:
                print(elapsed_seconds + 1)
                return

            # 4) 머리 추가
            snake_body.appendleft((next_x, next_y))
            snake_cells.add((next_x, next_y))

            # 5) 사과 처리 (사과 있으면 꼬리 안 뺐으니 길이 증가)
            if has_apple:
                grid[next_x][next_y] = 0

            elapsed_seconds += 1

    # 문제 설명상: "뱀이 전부 움직였거나" 명령을 다 수행하면 종료
    print(elapsed_seconds)

if __name__ == "__main__":
    main()