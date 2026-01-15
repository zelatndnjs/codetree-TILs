n,m,k = map(int, input().split())
grid = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    x,y = map(int, input().split())
    x -= 1
    y -= 1
    grid[x][y] = 1


def isin(n, x, y):
    return 0 <= x < n and 0 <= y < n


class Node:
    def __init__(self, x, y):
        self.x = x - 1
        self.y = y - 1
        self.prev = None
        self.next = None

class Snake:
    def __init__(self, head, tail):
        self.head = Node(1,1)
        self.tail = self.head

def isinsanke(snake: Snake, n: int) -> bool:
    node = snake.head
    while True:
        if node is None:
            return True
            break

        if isin(n, node.x, node.y):
            node = node.next
        else:
            return False
            break

def isCollape(snake: Snake) -> bool:
    node = snake.head
    t = []
    while True:
        if node is None:
            return False
            break
        else:
            if (node.x, node.y) in t:
                return True
                break
            else:
                t.append((node.x, node.y))
                node = node.next

def move(snake: Snake, grid: list, d: str, n: int) -> bool:
    if d == 'U':
        if isin(n, snake.head.x -1, snake.head.y):
            if grid[snake.head.x-1][snake.head.y] == 1:
                new = Node(snake.tail.x, snake.tail.y)
                node = snake.tail
                while True:
                    if node.prev is None:
                        break
                    else:
                        node.x = node.prev.x
                        node.y = node.prev.y
                        node = node.prev
                snake.tail.next = new
                new.prev = snake.tail
                snake.tail = new
                snake.head.x -= 1
                return True
            else:
                node = snake.tail
                while True:
                    if node.prev is None:
                        break
                    else:
                        node.x = node.prev.x
                        node.y = node.prev.y
                        node = node.prev
                snake.head.x -= 1
                return True
        else:
            return False
    elif d == 'D':
        if isin(n, snake.head.x + 1, snake.head.y):
            if grid[snake.head.x + 1][snake.head.y] == 1:
                new = Node(snake.tail.x, snake.tail.y)
                node = snake.tail
                while True:
                    if node.prev is None:
                        break
                    else:
                        node.x = node.prev.x
                        node.y = node.prev.y
                        node = node.prev
                snake.tail.next = new
                new.prev = snake.tail
                snake.tail = new
                snake.head.x += 1
                return True
            else:
                node = snake.tail
                while True:
                    if node.prev is None:
                        break
                    else:
                        node.x = node.prev.x
                        node.y = node.prev.y
                        node = node.prev
                snake.head.x += 1
                return True
        else:
            return False
    elif d == 'R':
        if isin(n, snake.head.x, snake.head.y + 1):
            if grid[snake.head.x][snake.head.y + 1] == 1:
                new = Node(snake.tail.x, snake.tail.y)
                node = snake.tail
                while True:
                    if node.prev is None:
                        break
                    else:
                        node.x = node.prev.x
                        node.y = node.prev.y
                        node = node.prev
                snake.tail.next = new
                new.prev = snake.tail
                snake.tail = new
                snake.head.y += 1
                return True
            else:
                node = snake.tail
                while True:
                    if node.prev is None:
                        break
                    else:
                        node.x = node.prev.x
                        node.y = node.prev.y
                        node = node.prev
                snake.head.y += 1
                return True
        else:
            return False
    else:
        if isin(n, snake.head.x, snake.head.y - 1):
            if grid[snake.head.x][snake.head.y - 1] == 1:
                new = Node(snake.tail.x, snake.tail.y)
                node = snake.tail
                while True:
                    if node.prev is None:
                        break
                    else:
                        node.x = node.prev.x
                        node.y = node.prev.y
                        node = node.prev
                snake.tail.next = new
                new.prev = snake.tail
                snake.tail = new
                snake.head.y -= 1
                return True
            else:
                node = snake.tail
                while True:
                    if node.prev is None:
                        break
                    else:
                        node.x = node.prev.x
                        node.y = node.prev.y
                        node = node.prev
                snake.head.y -= 1
                return True
        else:
            return False
node = Node(1,1)
snake = Snake(node, node)

answer = 0

chk = 0
for i in range(1, k+1):
    if chk == 1:
        break
    d, p = input().split()
    p = int(p)
    for _ in range(p):
        if move(snake, grid, d,n):
            if isCollape(snake):
                answer += 1
                chk = 1
                break
            else:
                answer += 1
        else:
            answer += 1
            chk = 1
            break

print(answer)