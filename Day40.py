def longest_balanced_subarray(numbers):
    prefix_sum = 0
    max_length = 0

    first_index = {0: -1}

    for i in range(len(numbers)):

        if numbers[i] == 0:
            prefix_sum -= 1
        else:
            prefix_sum += 1

        if prefix_sum in first_index:
            length = i - first_index[prefix_sum]
            max_length = max(max_length, length)
        else:
            first_index[prefix_sum] = i

    return max_length


numbers = [0, 1, 0, 1, 1, 0]

result = longest_balanced_subarray(numbers)

print(result)