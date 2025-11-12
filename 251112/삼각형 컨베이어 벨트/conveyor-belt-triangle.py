N,T = map(int, input().split())
belt = [list(map(int, input().split())) for _ in range(3)]
realbelt = belt[0] + belt[1] + belt[2]
realbelt *= 5
T = T % (3*N)
belt[0] = realbelt[3*N-T:4*N-T:]
belt[1] = realbelt[4*N-T:5*N-T:]
belt[2] = realbelt[5*N-T:6*N-T:]
print(*belt[0])
print(*belt[1])
print(*belt[2])