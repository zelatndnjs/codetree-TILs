def s(seat):
    n = len(seat)
    ans = 0
    for i in range(n):
        if seat[i] == '1':
            continue
        else:
            seat[i] = '1'
            minrange = 100
            for j in range(n-1):
                for k in range(j+1, n):
                    if seat[j] == '1' and seat[k] == '1':
                        minrange = min(minrange, k-j)
            ans = max(ans, minrange)
            seat[i] = '0'
    return ans

n = int(input())
seat = list(input())
print(s(seat))
