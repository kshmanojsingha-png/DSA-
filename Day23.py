def pivot_index(numbers):
    total_sum = 0

    for num in numbers:
        total_sum += num

    left_sum = 0

    for i in range(len(numbers)):
        right_sum = total_sum - left_sum - numbers[i]

        if left_sum == right_sum:
            return i

        left_sum += numbers[i]

    return -1

numbers = [1, 7, 3, 6, 5, 6]

result = pivot_index(numbers)

print("Pivot index:", result)