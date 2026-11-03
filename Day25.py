def longest_subarray(numbers, k):
    prefix_sum = 0
    max_length = 0

    first_index = {0: -1}

    for i, num in enumerate(numbers):
        prefix_sum += num

        required = prefix_sum - k

        if required in first_index:
            length = i - first_index[required]
            max_length = max(max_length, length)

        if prefix_sum not in first_index:
            first_index[prefix_sum] = i

    return max_length

numbers = [10, 5, 2, 7, 1, 9]
k = 15

result = longest_subarray(numbers, k)

print("Longest subarray length:", result)