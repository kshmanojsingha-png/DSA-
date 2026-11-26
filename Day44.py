def countInterestingSubarrays(nums, modulo, k):

    prefix = 0
    answer = 0

    freq = {0: 1}

    for num in nums:

        if num % modulo == k:
            prefix += 1

        required = (prefix - k) % modulo

        answer += freq.get(required, 0)

        current = prefix % modulo

        freq[current] = freq.get(current, 0) + 1

    return answer

nums = [3, 1, 9, 6]
modulo = 3
k = 0

result = countInterestingSubarrays(nums, modulo, k)

print("Count:", result)