num = [list(map(int, input().split())) for _ in range(2)]
print(f"{sum(num[0])/len(num[0]):.1f} {sum(num[1])/len(num[1]):.1f}")
print(f"{(num[0][0] + num[1][0])/2:.1f} {(num[0][1] + num[1][1])/2:.1f} {(num[0][2] + num[1][2])/2:.1f} {(num[0][3] + num[1][3])/2:.1f}")
print(f"{(sum(num[0]) + sum(num[1]))/8:.1f}")