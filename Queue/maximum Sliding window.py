from collections import deque

def max_in_sliding_window(nums, k):
    q = deque()  # Will store indexes of potential maximum elements
    result = []

    for i in range(len(nums)):
        # Remove elements out of current window
        if q and q[0] <= i - k:
            q.popleft()

        # Remove smaller elements (they are useless)
        while q and nums[i] >= nums[q[-1]]:
            q.pop()

        # Add current element's index
        q.append(i)

        # First window ready
        if i >= k - 1:
            result.append(nums[q[0]])

    return result

# Usage
arr = [10, 5, 2, 7, 8, 7]
k = 3
print(max_in_sliding_window(arr, k))
