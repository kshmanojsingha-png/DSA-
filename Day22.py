def build_prefix_sum(numbers):
    prefix = [0]

    for num in numbers:
        prefix.append(prefix[-1] + num)

    return prefix

def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]

numbers = [2, 4, 1, 7, 3]

prefix = build_prefix_sum(numbers)

result = range_sum(prefix, 1, 3)

print("Prefix Sum:", prefix)
print("Range Sum:", result)