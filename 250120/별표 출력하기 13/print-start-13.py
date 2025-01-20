n = int(input())
a=0
b=1
st = list()
for i in range(n):
    if i%2 == 0:
        for j in range(n-a):
            print('*', end=' ')
        print()
        st.append(n-a)
        a+=1
    else:
        for j in range(b):
            print('*', end=' ')
        print()
        st.append(b)
        b+=1
rest = list(reversed(st))
for i in rest:
    for j in range(i):
        print('*', end=' ')
    print()