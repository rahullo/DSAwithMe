###################
#### 3 #######

from typing import Counter


def longestword(string):
    list1 = {}
    maxi = 0
    count = 0
    for item in string:
        if item in list1:
            list1.clear()
            count = 0
            list1[item] = True
            count +=1

        if item not in list1:
            list1[item] = True
            count +=1
        maxi = max(maxi, count)
    return maxi

    
# print(longestword('dvdf'))


def convert(s, numRows):
    rows = [''] * numRows
    k = 0
    direction = (numRows == 1) - 1

    for c in s:
      rows[k] += c
      if k == 0 or k == numRows - 1:
        direction *= -1
      k += direction
      print(rows, k, direction)

    return ''.join(rows)

print(convert("PAYPALISHIRING", 4))