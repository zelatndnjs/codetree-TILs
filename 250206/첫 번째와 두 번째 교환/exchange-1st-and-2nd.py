a = list(input())
first = a[0]
second = a[1]
result = ""
for i in a:
    if i == first:
        result += second
    elif i == second:
        result += first
    else:
        result += i
print(result)