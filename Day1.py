def find_largest(numbers):
    largest = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]

    return largest


numbers = [12, 5, 27, 9, 18]

answer = find_largest(numbers)

print("Largest element:", answer)