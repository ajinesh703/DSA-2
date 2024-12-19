# Find Maximum Number

def find_max(arr):
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

# Example
print(find_max([3, 1, 4, 1, 5, 9]))
