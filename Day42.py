def count_divisible_subarrays(numbers, k):
    prefix_sum = 0
    count = 0

    frequency = {0: 1}

    for num in numbers:
        prefix_sum += num

        remainder = prefix_sum % k

        count += frequency.get(remainder, 0)

        frequency[remainder] = frequency.get(remainder, 0) + 1

    return count


numbers = [4, 5, 0, -2, -3, 1]
k = 5

result = count_divisible_subarrays(numbers, k)

print(result)