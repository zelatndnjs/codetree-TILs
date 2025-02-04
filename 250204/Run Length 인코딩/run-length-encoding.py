A = input()
A += '*'
answk = []
rotn = [0 for i in range(len(A))]
rotnidx = 0
for i in range(len(A)-1):
    if A[i] == A[i+1]:
        rotn[rotnidx] += 1
    else:
        answk.append(A[i])
        rotn[rotnidx] += 1
        rotnidx += 1
result = ""
for i in range(len(answk)):
    result += answk[i]
    result += str(rotn[i])

print(len(result))
print(result)
