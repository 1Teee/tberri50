def front_times(str, n):
  front3 = 3
  if len(str) < front3:
    return str[:front3] * n
  else:
    return str[:front3] * n