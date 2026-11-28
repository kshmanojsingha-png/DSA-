from collections import Counter


def minWindow(s, t):

    
    if not s or not t:
        return ""

    
    required_freq = Counter(t)

    
    window_freq = {}

    left = 0
    formed = 0

    required = len(required_freq)

    min_length = float("inf")
    start_index = 0

    
    for right in range(len(s)):

        char = s[right]

        window_freq[char] = window_freq.get(char, 0) + 1

        
        if char in required_freq:

            if window_freq[char] == required_freq[char]:
                formed += 1

        
        while formed == required:


            if right - left + 1 < min_length:

                min_length = right - left + 1
                start_index = left

            
            left_char = s[left]

            window_freq[left_char] -= 1


            if left_char in required_freq:

                if window_freq[left_char] < required_freq[left_char]:
                    formed -= 1

            left += 1


    if min_length == float("inf"):
        return ""

    return s[start_index:start_index + min_length]


s = "ADOBECODEBANC"
t = "ABC"

print("Minimum Window:", minWindow(s, t))