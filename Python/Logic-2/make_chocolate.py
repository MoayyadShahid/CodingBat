def make_chocolate(small, big, goal):
  if small + 5 * big < goal:
    return -1
  used = min(big, goal // 5)
  return goal - used * 5 if goal - used * 5 <= small else -1
