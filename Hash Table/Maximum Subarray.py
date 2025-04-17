def maxSubArrayLen(nums, k):
    prefix_sum = {0: -1}
    total = 0
    max_len = 0

    for i, num in enumerate(nums):
        total += num
        if total - k in prefix_sum:
            max_len = max(max_len, i - prefix_sum[total - k])
        if total not in prefix_sum:
            prefix_sum[total] = i
    return max_len
