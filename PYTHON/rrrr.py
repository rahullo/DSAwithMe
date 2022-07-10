from collections import Counter
def lengthOfLongestSubstring(s):
  # strings = {}
  # maxi = 0
  # leng = 0
  # for item in string:
  #   if item not in strings:
  #     strings[item] = True
  #     leng+=1
  #   elif item in strings:
  #     maxi = max(maxi, leng)
  #     leng = 0
  #     strings = {}
  #     strings[item] = True
  #     leng+=1
  #   maxi = max(maxi, leng)
  # return maxi
  ans = 0
  count = Counter()

  l = 0
  for r, c in enumerate(s):
    count[c] += 1
    print(r, c, ans, l , count)
    while count[c] > 1:
      count[s[l]] -= 1
      l += 1
    ans = max(ans, r - l + 1)

  return ans


# print(lengthOfLongestSubstring('abcabcbb'))
# print(lengthOfLongestSubstring('bbbbb'))
# print(lengthOfLongestSubstring('pwwkew'))
# print(lengthOfLongestSubstring('aab'))
print(lengthOfLongestSubstring('dvdf'))
