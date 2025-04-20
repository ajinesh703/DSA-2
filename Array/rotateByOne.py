def left_rotate_by_one(arr):
    if not arr:
        return []
    return arr[1:] + [arr[0]]

arr = [10, 20, 30, 40, 50]
print("Left Rotated:", left_rotate_by_one(arr))
