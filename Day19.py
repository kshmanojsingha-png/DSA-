def contains_duplicate(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return True

        seen.add(number)

    return False

numbers = [4, 7, 2, 7]

result = contains_duplicate(numbers)

print("Contains duplicate:", result)