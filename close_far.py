def close_far(a, b, c):
  if abs(a-b) <= 1 and abs(b-c) > 1:
    if abs(a-c) <= 1:
      return False
    return True
  elif abs(a-c) <= 1 and abs(b-c) > 1:
    return True
  else:
    return False
