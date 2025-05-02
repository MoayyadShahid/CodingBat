def sum67(nums):
  sum = 0
  skip = False
  for i in range(len(nums)):
    if nums[i] == 6:
      skip = True
    elif nums[i] == 7 and skip:
      skip = False
    elif skip:
      continue
    else:
      sum += nums[i]
  return sum
