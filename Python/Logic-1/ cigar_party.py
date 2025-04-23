def cigar_party(cigars, is_weekend):
  if is_weekend:
    return cigars >= 40
  else: 
    return True if 40<=cigars<=60 else False
