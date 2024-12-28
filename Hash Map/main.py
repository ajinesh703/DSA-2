def subarraySum(nums, k):
    hash_map = {0: 1}  # key: cumulative sum, value: count of occurrences
    cumulative_sum = 0
    count = 0
    
    for num in nums:
        cumulative_sum += num
        if cumulative_sum - k in hash_map:
            count += hash_map[cumulative_sum - k]
        hash_map[cumulative_sum] = hash_map.get(cumulative_sum, 0) + 1
    
    return count
    
# Example
nums = [1, 1, 1]
k = 2
print(subarraySum(nums, k))  # Output: 2
