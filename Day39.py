def count_subarrays(numbers, k):

    current_sum = 0
    count = 0

    frequency = {0: 1}

    for num in numbers:

        current_sum += num

        required_sum = current_sum - k

        count += frequency.get(required_sum, 0)

        frequency[current_sum] = frequency.get(current_sum, 0) + 1

    return count

numbers = [1, -1, 2, 3]
k = 2

result = count_subarrays(numbers, k)

print("Number of subarrays:", result)