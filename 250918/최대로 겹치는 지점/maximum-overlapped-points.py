# n = int(input())
# line = [0 for _ in range(101)]
# for i in range(n):
#     a,b = map(int, input().split())
#     for j in range(a,b+1):
#         line[j] += 1
# print(max(line))

n = int(input())
board = [0 for _ in range(101)]
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        board[i]+=1

print(max(board))
