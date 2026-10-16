def reverse_part(numbers, left, right):
    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
        right -= 1

def left_rotate(numbers, k):
    n = len(numbers)

    if n == 0:
        return numbers

    k = k % n

    reverse_part(numbers, 0, k - 1)
    reverse_part(numbers, k, n - 1)
    reverse_part(numbers, 0, n - 1)

    return numbers

numbers = [1, 2, 3, 4, 5, 6, 7]
k = 3

left_rotate(numbers, k)

print("Rotated array:", numbers)
