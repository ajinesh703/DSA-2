def findLeastNumOfUniqueInts(arr, k):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    freq_list = sorted(freq.values())
    removed = 0
    unique = len(freq_list)
    for f in freq_list:
        if k >= f:
            k -= f
            unique -= 1
        else:
            break
    return unique
