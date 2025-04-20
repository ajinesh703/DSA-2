def frequency_count(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

arr = [1, 2, 2, 3, 3, 3, 4]
print("Frequencies:", frequency_count(arr))
