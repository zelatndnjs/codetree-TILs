for i in range(1,20):
    for j in range(1, 20):
        if j % 2 == 1:
            if j == 19:
                print(f"{i} * {j} = {i * j}")
            else:
                print(f"{i} * {j} = {i * j}", end=' / ')
        else:
            print(f"{i} * {j} = {i * j}")