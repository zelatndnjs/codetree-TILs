a = input()
arr= list(a)
arr.pop(a.index('e'))
result = "".join(arr)
print(result)