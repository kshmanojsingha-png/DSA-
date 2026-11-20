def count_subarrays(numbers, goal):

    current_sum = 0
    count = 0

    prefix_frequency = {0: 1}

    for num in numbers:

        current_sum += num

        needed = current_sum - goal

        count += prefix_frequency.get(needed, 0)

        prefix_frequency[current_sum] = (
            prefix_frequency.get(current_sum, 0) + 1
        )

    return count


numbers = [1, 0, 1, 0, 1]
goal = 2

result = count_subarrays(numbers, goal)

print("Number of subarrays:", result)