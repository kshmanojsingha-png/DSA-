def first_occurrence(numbers, target):
    left = 0
    right = len(numbers) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            result = mid
            right = mid - 1
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

def last_occurrence(numbers, target):
    left = 0
    right = len(numbers) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            result = mid
            left = mid + 1
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

def count_occurrences(numbers, target):
    first = first_occurrence(numbers, target)

    if first == -1:
        return 0

    last = last_occurrence(numbers, target)

    return last - first + 1

numbers = [1, 2, 2, 2, 2, 3, 4, 5]
target = 2

print("Occurrences:", count_occurrences(numbers, target))