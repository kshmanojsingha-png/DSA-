def min_subarray_length(target, numbers):

    left = 0
    current_sum = 0
    min_length = len(numbers) + 1

    for right in range(len(numbers)):

        current_sum += numbers[right]

        while current_sum >= target:

            current_length = right - left + 1

            min_length = min(min_length, current_length)

            current_sum -= numbers[left]
            left += 1

    if min_length == len(numbers) + 1:
        return 0

    return min_length

numbers = [2, 3, 1, 2, 4, 3]
target = 7

result = min_subarray_length(target, numbers)

print("Minimum subarray length:", result)