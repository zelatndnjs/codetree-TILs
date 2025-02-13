def f(a,o,c):
    a = int(a)
    c = int(c)
    if o == '+':
        print(f"{a} + {c} = {a+c}")
    elif o == '-':
        print(f"{a} - {c} = {a-c}")
    elif o == '*':
        print(f"{a} * {c} = {a*c}")
    elif o == '/':
        print(f"{a} / {c} = {a//c}")
    else:
        print("False")


a,o,c = input().split()
f(a,o,c)