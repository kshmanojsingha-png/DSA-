def integer_sqrt(x):
    if x < 2:
        return x

    left = 1
    right = x // 2
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == x:
            return mid

        elif square < x:
            answer = mid
            left = mid + 1

        else:
            right = mid - 1

    return answer

x = 30

print("Integer square root:", integer_sqrt(x))