def total_fruit(fruits):

    left = 0
    frequency = {}
    max_fruits = 0

    for right in range(len(fruits)):

        fruit = fruits[right]

        frequency[fruit] = frequency.get(fruit, 0) + 1

        while len(frequency) > 2:

            left_fruit = fruits[left]

            frequency[left_fruit] -= 1

            if frequency[left_fruit] == 0:
                del frequency[left_fruit]

            left += 1

        current_length = right - left + 1

        max_fruits = max(max_fruits, current_length)

    return max_fruits


fruits = [1, 2, 1, 2, 3]

result = total_fruit(fruits)

print("Maximum fruits collected:", result)