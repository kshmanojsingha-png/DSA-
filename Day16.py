def search_rotated(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        if numbers[left] <= numbers[mid]:

            # Check whether target belongs to the left half
            if numbers[left] <= target < numbers[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:

            # Check whether target belongs to the right half
            if numbers[mid] < target <= numbers[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

numbers = [4, 5, 6, 7, 0, 1, 2]
target = 0

result = search_rotated(numbers, target)

print("Target index:", result)