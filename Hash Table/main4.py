def two_sum(nums, target):
    num_map = {}  # Store value:index pairs
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]  # Return indices
        num_map[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
