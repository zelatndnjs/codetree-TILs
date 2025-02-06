s, q = input().split()
q = int(q)
result = s
for i in range(q):
    new = ''
    num, a,b = input().split()
    if num == '1':
        l = list(result)
        tmp = l[int(a)-1]
        l[int(a)-1] = l[int(b)-1]
        l[int(b)-1] = tmp
        result = ''.join(l)
        print(result)
    elif num == '2':
        l = list(result)
        for i in l:
            if i == a:
                new += b
            else:
                new += i
        result = new
        print(result)