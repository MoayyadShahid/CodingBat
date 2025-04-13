def not_string(str):
  if len(str) < 3:
    return 'not ' + str
  elif str[:3] == 'not':
    return str
  else:
    return 'not ' + str