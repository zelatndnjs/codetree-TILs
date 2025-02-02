a, b = input().split()
result = ""
if len(a) > len(b):
  result = a
  print(f"{result} {len(result)}")
elif len(a) < len(b):
  result = b
  print(f"{result} {len(result)}")
else:
  result = "same"
  print(f"{result}")
