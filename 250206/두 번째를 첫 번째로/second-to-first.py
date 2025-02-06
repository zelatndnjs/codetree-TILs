arr = list(input())
first = arr[0]
second = arr[1]
result =""
for i in arr:
    if i == second:
        result += first
    else:
        result += i
print(result)