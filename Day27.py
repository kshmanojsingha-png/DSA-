def max_subarray(numbers):
    current_sum = numbers[0]
    max_sum = numbers[0]

    temp_start = 0
    start = 0
    end = 0

    for i in range(1, len(numbers)):

        if numbers[i] > current_sum + numbers[i]:
            current_sum = numbers[i]
            temp_start = i
        else:
            current_sum += numbers[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, start, end

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum, start, end = max_subarray(numbers)

print("Maximum Sum:", max_sum)
print("Starting Index:", start)
print("Ending Index:", end)
print("Maximum Subarray:", numbers[start:end + 1])