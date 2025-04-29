def round10(num):
  rem = num % 10
  if rem >= 5:
    return (num // 10 + 1) * 10
  else:
    return (num // 10) * 10

def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
