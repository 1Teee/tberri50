def sum67(nums):
  switch = True
  sum = 0
  for num in nums:
    if num == 6:
      switch = False
    elif switch == False and num == 7:
      switch = True
    elif switch:
      sum += num
  return sum
