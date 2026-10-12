def move_zeroes(numbers):
    position = 0

    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[position], numbers[i] = numbers[i], numbers[position]
            position += 1

    return numbers

numbers = [0, 1, 0, 3, 12]

answer = move_zeroes(numbers)

print("After moving zeroes:", answer)
