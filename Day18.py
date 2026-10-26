def two_sum(numbers, target):
    seen = {}

    for i in range(len(numbers)):
        complement = target - numbers[i]

        if complement in seen:
            return [seen[complement], i]

        seen[numbers[i]] = i

    return []

numbers = [2, 7, 11, 15]
target = 9

result = two_sum(numbers, target)

print("Indices:", result)