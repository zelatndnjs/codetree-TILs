c = ['apple', 'banana', 'grape', 'blueberry','orange']
a = input()
cnt = 0
for i in c:
    if i[2] == a or i[3] == a:
        print(i)
        cnt += 1
print(cnt)