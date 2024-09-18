def front3(str):
  front3 = 3
  if len(str) < front3:
    front3 = len(str)
  f = str[:front3]
  return f + f + f
