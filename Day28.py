def three_sum(numbers):
    numbers.sort()

    triplets = []
    n = len(numbers)

    for i in range(n - 2):

        if i > 0 and numbers[i] == numbers[i - 1]:
            continue

        if numbers[i] > 0:
            break

        left = i + 1
        right = n - 1

        while left < right:
            total = numbers[i] + numbers[left] + numbers[right]

            if total < 0:
                left += 1

            elif total > 0:
                right -= 1

            else:
                triplets.append([
                    numbers[i],
                    numbers[left],
                    numbers[right]
                ])

                left += 1
                right -= 1

                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1

                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1

    return triplets

numbers = [-1, 0, 1, 2, -1, -4]

result = three_sum(numbers)

print("Unique triplets:", result)