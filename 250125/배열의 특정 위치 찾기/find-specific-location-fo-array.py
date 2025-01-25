num = list(map(int, input().split()))

print(f"{sum(num[1::2])} {sum(num[2::3])/len(num[2::3]):.1f}")