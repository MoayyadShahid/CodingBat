def centered_average(nums):
  max = nums[0]
  min = nums[0]
  sum = 0
  for i in nums:
    sum += i
    if max < i:
      max = i
    elif min > i:
      min = i
  return (sum - max - min) / (len(nums) - 2)
