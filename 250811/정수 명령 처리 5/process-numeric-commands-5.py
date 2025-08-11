n = int(input())
arr = []
for i in range(n):
    c = input()
    if c == 'size':
        print(len(arr))
    elif c == 'pop_back':
        arr.pop()
    else:
        a,b = c.split()
        b = int(b)
        if a == 'push_back':
            arr.append(b)
        elif a == 'get':
            print(arr[b-1])
        else:
            print("error")
