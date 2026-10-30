def first_unique_char(s):
    frequency = {}

    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    # Second pass: Find the first unique character
    for i, char in enumerate(s):
        if frequency[char] == 1:
            return i

    return -1

s = "leetcode"

result = first_unique_char(s)

print("First unique character index:", result)