def dis(seat):
    d = 1000
    for i in range(len(seat)-1):
        for j in range(i+1, len(seat)):
            if seat[i] == '1' and seat[j] == '1':
                d = min(d, j-i)
    return d

n = int(input())
seat = list(input())
maxd = 0
for i in range(n-1):
    for j in range(i+1, n):
        if seat[i] == '0' and seat[j] == '0':
            seat[i] = '1'
            seat[j] = '1'
            maxd = max(maxd, dis(seat))
            seat[i] = '0'
            seat[j] = '0'
print(maxd)
