def last2(str):
  if len(str) < 2:
    return 0
  
  last = str[-2:]
  counter = 0
  
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last:
      counter += 1
      
  return counter
    
