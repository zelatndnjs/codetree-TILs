def count_beatiful_numbers(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif n == 4:
        return 8
    else:
        return count_beatiful_numbers(n-1) + count_beatiful_numbers(n-2) + count_beatiful_numbers(n-3) + count_beatiful_numbers(n-4)

n = int(input())
print(count_beatiful_numbers(n))