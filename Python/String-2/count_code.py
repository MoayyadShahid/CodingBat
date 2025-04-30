def count_code(str):
  str_l = str.lower()
  sum = 0
  for i in range(65, 92):
    sum += str_l.count("co"+chr(i).lower()+"e")
  return sum
    
    
