def sum2(nums):
  size = len(nums)
  if size == 0: return 0
  if size < 2: return nums[0]
  else: return nums[0] + nums[1]
