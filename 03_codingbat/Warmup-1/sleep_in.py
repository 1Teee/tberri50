def sleep_in(weekday, vacation):
  if not weekday and not vacation:
    return True
  if vacation:
    return True
  elif weekday:
    return False
