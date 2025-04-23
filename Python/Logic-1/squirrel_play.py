def squirrel_play(temp, is_summer):
  if is_summer:
    return True if 60<=temp<=100 else False
  else:
    return True if 60<=temp<=90 else False
