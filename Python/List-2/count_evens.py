def count_evens(nums):
  ct = 0
  for i in nums:
    if i % 2 == 0:
      ct += 1
  return ct
