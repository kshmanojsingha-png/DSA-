def max_sum_subarray(numbers, k):
    if k <= 0 or k > len(numbers):
        return None

    window_sum = 0

    for i in range(k):
        window_sum += numbers[i]

    max_sum = window_sum

    for i in range(k, len(numbers)):
        window_sum += numbers[i]
        window_sum -= numbers[i - k]

        max_sum = max(max_sum, window_sum)

    return max_sum

numbers = [2, 1, 5, 1, 3, 2]
k = 3

result = max_sum_subarray(numbers, k)

print("Maximum subarray sum:", result)