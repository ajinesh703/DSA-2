def move_zeros(nums):
  
  non_zero_ptr = 0
  
  for i in range(len(nums)):
    if nums[i] != 0:
      nums[non_zero_ptr], nums[i] = nums[i], nums[non_zero_ptr]
      non_zero_ptr += 1
      
  for i in range(non_zero_ptr, len(nums)):
    nums[i] = 0
  
  return nums
