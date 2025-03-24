p = input()
arr = ["apple","banana","grape","blueberry","orange"]
cnt =0
for i in arr:
    if i[2] == p or i[3]==p:
        print(i)
        cnt += 1
print(cnt)