def rotate_right(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("Rotated Array:", rotate_right(arr, k))  # Output: [5, 6, 7, 1, 2, 3, 4]
