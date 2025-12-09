a = input()

def shift(a):
    a = a[1::] + a[0]
    return a

def enc(a):
    new = a[0]
    i = 0
    nums = []
    num = 1
    while True:
        if a[i] == a[i+1]:
            i+=1
            num += 1
        else:
            new += a[i+1]
            i += 1
            nums.append(str(num))
            num = 1
        if i >= len(a)-1:
            nums.append(str(num))
            break
    new  = new + ''.join(nums)
    return new
if len(a) == 1:
    answer = 2
else:
    for i in range(len(a)-1):
        answer = min(answer, len(enc(a)))
        a = shift(a)
print(answer)