n,m = map(int, input().split())
sq1 = [list(map(int, input().split())) for _ in range(n)]
sq2 = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if sq1[i][j] != sq2[i][j]:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()