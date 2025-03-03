def minSetSize(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    freq_list = sorted(freq.values(), reverse=True)
    total = 0
    count = 0
    for f in freq_list:
        total += f
        count += 1
        if total >= len(arr)//2:
            break
    return count
