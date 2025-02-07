string = input()
for i in range(len(string)):
    newString = string[-1::] + string[:-1:]
    print(newString)
    string  = newString