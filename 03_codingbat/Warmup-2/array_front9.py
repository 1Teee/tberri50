def array_front9(nums):
  end = len(nums)
  if end > 4:
    end = 4
  
  nums2 = nums[:end]
  if nums2.count(9) > 0:
    return True
  else:
    return False
