def countEqualSubarrays(arr):

    count0 = 0
    count1 = 0
    count2 = 0

    freq = {(0, 0): 1}

    answer = 0

    for num in arr:

        if num == 0:
            count0 += 1

        elif num == 1:
            count1 += 1

        else:
            count2 += 1

        diff1 = count1 - count0
        diff2 = count2 - count0

        key = (diff1, diff2)

        if key in freq:
            answer += freq[key]

        freq[key] = freq.get(key, 0) + 1

    return answer


arr = [0, 1, 2, 0, 1, 2]

result = countEqualSubarrays(arr)

print("Number of valid subarrays:", result)