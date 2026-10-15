def left_rotate(numbers):
    if len(numbers) == 0:
        return numbers

    first = numbers[0]

    for i in range(len(numbers) - 1):
        numbers[i] = numbers[i + 1]

    numbers[len(numbers) - 1] = first

    return numbers

numbers = [1, 2, 3, 4, 5]

answer = left_rotate(numbers)

print("After left rotation:", answer)
