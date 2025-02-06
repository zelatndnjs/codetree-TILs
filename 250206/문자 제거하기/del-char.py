arr = list(input())
result = "".join(arr)
while True:
    if len(result) == 1:
        break
    num = int(input())
    if num >= len(result):
        num = -1
    arr.pop(num)
    result = "".join(arr)
    print(result)
    arr = list(result)