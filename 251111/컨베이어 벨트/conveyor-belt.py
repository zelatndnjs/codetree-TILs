N, T = map(int, input().split())
belt = [list(map(int, input().split())) for _ in range(2)]
realbelt = belt[0] + belt[1]
realbelt = realbelt * 4
T = T % (2*N)
belt[0] = realbelt[2*N-T:2*N-T+N:]
belt[1] = realbelt[2*N-T+N:2*N-T+2*N]
for i in range(2):
    for j in range(N):
        print(belt[i][j], end=' ')
    print()