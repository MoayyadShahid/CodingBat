def centered_average(nums):
  nums.sort()
  max = nums[-1]
  min = nums[0]
  return (sum(nums) - max - min) / (len(nums) - 2)
