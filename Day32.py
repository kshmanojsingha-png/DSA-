def longest_subarray_at_most_k(numbers, k):

    if k < 0:
        return 0

    left = 0
    window_sum = 0
    max_length = 0

    for right in range(len(numbers)):

        window_sum += numbers[right]

        while window_sum > k:
            window_sum -= numbers[left]
            left += 1

        current_length = right - left + 1

        max_length = max(max_length, current_length)

    return max_length

numbers = [2, 1, 5, 1, 3, 2]
k = 7

result = longest_subarray_at_most_k(numbers, k)

print("Longest subarray length:", result)