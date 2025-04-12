def array_front9(nums):
  pos = 0
  for i in nums:
    if pos < 4 and nums[pos] == 9:
      return True
    pos += 1
        
  return False
