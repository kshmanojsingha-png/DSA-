def search_insert(numbers, target):
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

    return left

numbers = [1, 3, 5, 6]
target = 2

result = search_insert(numbers, target)

print("Insert position:", result)