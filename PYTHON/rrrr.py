def moveZeroes(nums):
  i = len(nums) -1
  if len(nums) <=1:
    return nums

  while i >=0:
    if nums[i] ==0:
      del nums[i]
      nums.append(0)
    i-=1

  return nums

print(moveZeroes([0]))