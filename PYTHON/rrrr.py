class Solution:
  def rotate(self, nums, k: int) -> None:
    k %= len(nums)
    self.reverse(nums, 0, len(nums) - 1)
    self.reverse(nums, 0, k - 1)
    self.reverse(nums, k, len(nums) - 1)
    return nums

  def reverse(self, nums, l: int, r: int) -> None:
    print('\n')
    while l < r:
      print(nums, l, r)
      nums[l], nums[r] = nums[r], nums[l]
      l += 1
      r -= 1
    return nums

s = Solution()
# print(s.rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(s.reverse([1, 2, 3, 4, 5, 6, 7], 0, 6))