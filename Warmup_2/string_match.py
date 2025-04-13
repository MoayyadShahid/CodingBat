def string_match(a, b):
  min_len = len(a) if len(a) <= len(b) else len(b)
  count = 0
  if min_len < 2:
    return 0
  
  for i in range(min_len - 1):
    if(a[i] == b[i] and a[i+1] == b[i+1]):
      count += 1
  
  return count
