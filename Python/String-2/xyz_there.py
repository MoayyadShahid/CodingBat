def xyz_there(str):
  if ".xyz" in str:
    if str.count("xyz") == str.count(".xyz"):
      return False
    else:
      return True
  elif str.count("xyz") >= 1:
    return True
  else:
    return False
