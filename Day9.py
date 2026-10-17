def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i

    return -1

numbers = [10, 25, 30, 45, 50]
target = 30

result = linear_search(numbers, target)

print("Target index:", result)