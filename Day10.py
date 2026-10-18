def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        elif numbers[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1

numbers = [10, 20, 30, 40, 50, 60, 70]
target = 50

result = binary_search(numbers, target)

print("Target index:", result)