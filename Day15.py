def find_peak_element(numbers):
    left = 0
    right = len(numbers) - 1

    while left < right:
        mid = (left + right) // 2

        if numbers[mid] < numbers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left

numbers = [1, 2, 3, 1]

index = find_peak_element(numbers)

print("Peak index:", index)
print("Peak element:", numbers[index])