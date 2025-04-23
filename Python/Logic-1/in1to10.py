def in1to10(n, outside_mode):
  if outside_mode:
    return True if not(1<n<10) else False
  else:
    return True if 1<=n<=10 else False
