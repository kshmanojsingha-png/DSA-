def is_sorted(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            return False

    return True

numbers = [1, 2, 3, 4, 5]

answer = is_sorted(numbers)

print("Is the array sorted?", answer)