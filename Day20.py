def is_anagram(s, t):
    if len(s) != len(t):
        return False

    frequency = {}

    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    for char in t:
        if char not in frequency:
            return False

        frequency[char] -= 1

        if frequency[char] < 0:
            return False

    return True

s = "listen"
t = "silent"

result = is_anagram(s, t)

print("Are the strings anagrams?", result)