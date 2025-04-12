def string_bits(str):
  pos = 0
  bits = ''
  while(pos < len(str)):
    bits += str[pos]
    pos += 2
  
  return bits
    