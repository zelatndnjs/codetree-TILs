while True:
    A = input()
    if A == 'END':
        break
    else:
        A = list(A)
        A = reversed(A)
        result = "".join(A)
        print(result)