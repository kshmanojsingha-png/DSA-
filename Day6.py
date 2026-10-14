def remove_duplicates(numbers):
    if len(numbers) == 0:
        return 0

    unique_index = 0

    for i in range(1, len(numbers)):
        if numbers[i] != numbers[unique_index]:
            unique_index += 1
            numbers[unique_index] = numbers[i]

    return unique_index + 1

numbers = [1, 1, 2, 2, 3, 4, 4]

count = remove_duplicates(numbers)

print("Number of unique elements:", count)
print("Unique elements:", numbers[:count])