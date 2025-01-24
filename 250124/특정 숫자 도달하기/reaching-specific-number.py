l = list(map(int, input().split()))
newl = list()
for i in l:
    if i >= 250:
        break
    else:
        newl.append(i)

print(f"{sum(newl)} {sum(newl)/len(newl):.1f}")