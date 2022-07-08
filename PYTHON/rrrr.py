from audioop import reverse


def findMedianSortedArrays(nums1, nums2):
  merged = nums1 + nums2
  merged.sort(reverse=False)
  lenMerged = len(nums1)+len(nums2)
  mid = lenMerged//2
  if lenMerged % 2 == 0:
    return ( merged[mid-1] + merged[mid])/2
  else:
    return merged[mid]

print(findMedianSortedArrays([1, 2], [3, 4]))