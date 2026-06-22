def combo_string(a, b):
  if len(b) > len(a):
    short = a
    long = b
  elif len(a) > len(b):
    short = b
    long = a
  else:
    short = a
    long = b
  return short + long + short
