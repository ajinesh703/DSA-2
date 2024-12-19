# Minimum Element in Array

def find_min(arr):
  
  min_element = arr[0]
  
  for num in arr:
    if num < min_element:
      min_element = num
      
  return min_element

# Example//

print(find_min([4, 2, 5, 8, 9]))
