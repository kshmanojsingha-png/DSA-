# Problem-1 Find the Second Largest Element
# Given an array of integers, find the second-largest distinct element without using max() or sorting.

def second_largest(numbers):
    if len(numbers) < 2:
        return None

    largest = numbers[0]
    second = None

    for num in numbers[1:]:
        if num > largest:
            second = largest
            largest = num

        elif num != largest:
            if second is None or num > second:
                second = num

    return second

print(second_largest([12, 5, 27, 9, 18]))

# Problem-2 Move Zeroes to the End
# Move all zeroes to the end of the array while maintaining the original order of non-zero elements.

def move_zeroes(numbers):
    position = 0

    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[position], numbers[i] = numbers[i], numbers[position]
            position += 1

    return numbers

print(move_zeroes([0, 1, 0, 3, 12]))

# Problem-3 Binary Search
# Given a sorted array and a target, return its index. Return -1 if it doesn't exist.

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        elif numbers[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1

numbers = [10, 20, 30, 40, 50, 60]

print(binary_search(numbers, 40))

# Problem-4 Two Sum
# Given an array and a target, return the indices of two different elements whose sum equals the target.

def two_sum(numbers, target):
    seen = {}

    for i in range(len(numbers)):
        complement = target - numbers[i]

        if complement in seen:
            return [seen[complement], i]

        seen[numbers[i]] = i

    return []

print(two_sum([2, 7, 11, 15], 9))

# Problem-5 Count Subarrays with Sum K
# Given an integer array and a target K, count how many continuous subarrays have a sum equal to K.

def subarray_sum(numbers, k):
    prefix_sum = 0
    count = 0

    frequency = {0: 1}

    for num in numbers:
        prefix_sum += num

        required = prefix_sum - k

        if required in frequency:
            count += frequency[required]

        frequency[prefix_sum] = frequency.get(prefix_sum, 0) + 1

    return count

print(subarray_sum([1, 1, 1], 2))

# Problem-6 Maximum Subarray Sum
# Find the maximum sum of a non-empty continuous subarray.

def max_subarray_sum(numbers):
    current_sum = numbers[0]
    max_sum = numbers[0]

    for i in range(1, len(numbers)):
        current_sum = max(numbers[i], current_sum + numbers[i])

        max_sum = max(max_sum, current_sum)

    return max_sum

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(max_subarray_sum(numbers))