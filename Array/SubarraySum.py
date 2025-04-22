def subarray_sum(nums, k):
    count = 0                       # Number of subarrays that sum to k
    current_sum = 0                # Running sum (prefix sum)
    prefix_map = {0: 1}            # Map to store count of prefix sums

    for num in nums:
        current_sum += num         # Add current number to running sum

        # Check if there's a prefix sum that when subtracted from current_sum gives k
        if (current_sum - k) in prefix_map:
            count += prefix_map[current_sum - k]  # Add number of times that prefix was seen

        # Record current prefix sum in map
        if current_sum in prefix_map:
            prefix_map[current_sum] += 1
        else:
            prefix_map[current_sum] = 1

    return count
