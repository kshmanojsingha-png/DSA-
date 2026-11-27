def atMostK(nums, k):

    if k < 0:
        return 0

    left = 0
    count = 0
    freq = {}

    for right in range(len(nums)):

        
        freq[nums[right]] = freq.get(nums[right], 0) + 1

        while len(freq) > k:

            freq[nums[left]] -= 1

            if freq[nums[left]] == 0:
                del freq[nums[left]]

            left += 1

        count += right - left + 1

    return count


def subarraysWithKDistinct(nums, k):

    return atMostK(nums, k) - atMostK(nums, k - 1)

nums = [1, 2, 1, 2, 3]
k = 2

result = subarraysWithKDistinct(nums, k)

print("Answer:", result)