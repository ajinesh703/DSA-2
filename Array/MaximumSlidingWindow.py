from collections import deque

def max_sliding_window(nums, k):
    output = []           # List to store the result (max in each window)
    q = deque()           # Will store **indices** of potential max elements
    left = 0              # Left edge of window

    for right in range(len(nums)):  # Move the right edge of the window
        # Step 1: Remove elements from back of deque if they are smaller than the current element
        while q and nums[q[-1]] < nums[right]:
            q.pop()  # They can’t be the max if current is greater

        # Step 2: Add the current element’s index to deque
        q.append(right)

        # Step 3: Remove indices from the front if they are outside the current window
        if q[0] < left:
            q.popleft()

        # Step 4: Once the window has reached size k, record the max (at the front of the deque)
        if right + 1 >= k:
            output.append(nums[q[0]])  # Front of deque has the index of max element
            left += 1  # Slide the window forward

    return output
