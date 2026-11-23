def longest_zero_sum_subarray(numbers):
    prefix_sum = 0
    max_length = 0

    first_index = {0: -1}

    for i in range(len(numbers)):
        prefix_sum += numbers[i]

        if prefix_sum in first_index:
            length = i - first_index[prefix_sum]
            max_length = max(max_length, length)
        else:
            first_index[prefix_sum] = i

    return max_length


numbers = [1, 2, -3, 3, -1]

result = longest_zero_sum_subarray(numbers)

print(result)