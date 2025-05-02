def sum13(nums):
  sum = 0
  skip = False
  for i in range(len(nums)):
    if nums[i] == 13:
      skip = True
    elif skip:
      skip = False
      continue
    else:
      sum += nums[i]   
  return sum
    