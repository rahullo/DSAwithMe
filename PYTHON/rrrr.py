def twoSum(numbers, target):
  l = 0
  r = len(numbers)-1
  while l<r:
    sum = numbers[l] + numbers[r]
    if sum == target:
      return [l+1, r+1]
    elif sum < target:
      l+=1
    else:
      r-=1

print(twoSum([0, 0, 11, 15], 0))

# li = [1, 2, 3, 4, 5]
# ans = li[2:]

# print(ans)