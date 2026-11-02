def subarray_sum(numbers, k):
    prefix_sum = 0
    count = 0

    frequency = {0: 1}

    for num in numbers:
        prefix_sum += num

        required = prefix_sum - k

        if required in frequency:
            count += frequency[required]

        frequency[prefix_sum] = frequency.get(prefix_sum, 0) + 1

    return count

numbers = [1, 1, 1]
k = 2

result = subarray_sum(numbers, k)

print("Number of subarrays:", result)