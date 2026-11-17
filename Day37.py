def character_replacement(s, k):

    left = 0
    frequency = {}
    max_length = 0

    for right in range(len(s)):

        char = s[right]

        frequency[char] = frequency.get(char, 0) + 1

        max_frequency = max(frequency.values())

        window_size = right - left + 1

        while window_size - max_frequency > k:

            left_char = s[left]

            frequency[left_char] -= 1

            if frequency[left_char] == 0:
                del frequency[left_char]

            left += 1

            window_size = right - left + 1
            max_frequency = max(frequency.values())

        max_length = max(max_length, window_size)

    return max_length


s = "AABABBA"
k = 1

result = character_replacement(s, k)

print("Longest repeating substring length:", result)