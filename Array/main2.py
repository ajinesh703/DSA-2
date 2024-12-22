def maxProduct(nums):
    max_product = min_product = result = nums[0]

    for num in nums[1:]:
        if num < 0:
            max_product, min_product = min_product, max_product
        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)
        result = max(result, max_product)

    return result

# Example
nums = [2, 3, -2, 4]
print(maxProduct(nums))  # Output: 6
