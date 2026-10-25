def find_min(numbers):
    left = 0
    right = len(numbers) - 1

    while left < right:
        mid = (left + right) // 2

        if numbers[mid] > numbers[right]:
            left = mid + 1
        else:
            right = mid

    return numbers[left]

numbers = [4, 5, 6, 7, 0, 1, 2]

result = find_min(numbers)

print("Minimum element:", result)