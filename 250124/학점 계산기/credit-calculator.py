n = int(input())
num = list(map(float, input().split()))
avg = sum(num) / len(num)
print(f"{avg:.1f}")
if avg >=4.0:
    print("Perfect")
elif avg >=3.0:
    print("Good")
else:
    print("Poor")