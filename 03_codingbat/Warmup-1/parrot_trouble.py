def parrot_trouble(talking, hour):
  if not talking:
    return False
  elif talking and ((hour < 7) or (hour > 20)):
    return  True
  elif talking and ((hour > 7) or (hour < 20)):
    return False
