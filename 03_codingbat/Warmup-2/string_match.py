def string_match(a, b):
  shorter = min(len(a), len(b))
  counter = 0
  
  for i in range(shorter-1):
    aS = a[i:i+2]
    bS = b[i:i+2]
    if aS == bS:
      counter += 1
  return counter
