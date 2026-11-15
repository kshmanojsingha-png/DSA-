def longest_substring_k_distinct(s, k):

    if k <= 0:
        return 0

    left = 0
    frequency = {}
    max_length = 0

    for right in range(len(s)):

        char = s[right]

        frequency[char] = frequency.get(char, 0) + 1

        while len(frequency) > k:

            left_char = s[left]

            frequency[left_char] -= 1

            if frequency[left_char] == 0:
                del frequency[left_char]

            left += 1

        current_length = right - left + 1

        max_length = max(max_length, current_length)

    return max_length


s = "eceba"
k = 2

result = longest_substring_k_distinct(s, k)

print("Longest substring length:", result)