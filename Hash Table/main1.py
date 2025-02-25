def intersection(nums1, nums2):
    set1 = set(nums1)  # Convert to set for O(1) lookups
    result = []
    for num in nums2:
        if num in set1:
            result.append(num)
            set1.remove(num)  # Avoid duplicates
    return result

print(intersection([1,2,2,1], [2,2]))  # Output: [2]
