def f(string, num):
    if num == 1:
        return string[1::] + string[0]
    elif num == 2:
        return string[-1] + string[:-1:]
    elif num == 3:
        return "".join(reversed(string))
    else:
        print("Wring num!")

string, q = input().split()
q = int(q)
for i in range(q):
    num = int(input())
    result = f(string, num)
    print(result)
    string = result
