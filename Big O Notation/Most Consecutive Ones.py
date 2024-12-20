def find_max_consecutive_ones(nums):
    max_ones = count = 0
    for num in nums:
        if num == 1:
            count += 1
            max_ones = max(max_ones, count)
        else:
            count = 0
    return max_ones

# Example
print(find_max_consecutive_ones([1, 1, 0, 1, 1, 1]))  # Output: 3
