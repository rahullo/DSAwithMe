array = [5, 2, 9, 0, -1]
def finding_minimum(array):
    minimum = array[0]
    for i in range(len(array)):
        if(array[i] < minimum):
            minimum = array[i]
    return minimum

print(finding_minimum(array))

array = [5, 2, 9, 0, -1]
array.sort()
print(array)

array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selectionSort(array):
    for i in range(len(array)):
        mini = i
        temp = array[i]
        for j in range(i+1, len(array)):
            if(array[j] < array[mini]):
                mini = j

        array[i] = array[mini]
        array[mini] = temp

    return array

selectionSort(array)
print(array)




def newArray(array, i, j):
    answer = []
    for item in range(i, j+1):
        answer.append(array[item])

    return answer

# print(newArray([1, 2, 3, 4, 5, 6, 7], 1, 4))

def merge(left, right):
    result = []
    leftIndex = 0
    rightIndex =0 
    while(leftIndex < len(left) and rightIndex < len(right)):
        if(left[leftIndex] < right[rightIndex]):
            result.append(left[leftIndex])
            leftIndex+=1

        else:
            result.append(right[rightIndex])
            rightIndex+=1
    return result+(newArray(left, leftIndex, len(left)-1) + newArray(right, rightIndex, len(right)-1))

print(merge([3], [2, 4]))

array = [5, 2, 9, 0, -1]

array.append(9)
array2 = array.copy()
print(array.count())
array.extend([11, 12, 13])
print(array.index(11))
array.insert(5, 4)
array.pop(2)
array.remove(2)
array.reverse()
array.sort()
print( array)

from random import randint, random

from numpy import cumsum


print(randint(1, 6))
import time

t = time.localtime()

current_time = time.strftime("%H:%M", t)
print(t)
print(time)
print(current_time)

start = 1
end = 25
for num in range(start, end):
    for i in range(2, num):
        if(num%i) == 0:
            break
    else:
        print(num)


for i in range(4):
        print([1]*(i+1))


class Find_Missing():
    def missing(self, arr, n):
        sum=0
        for i in range(n-1):
            sum += arr[i]
        
        # print(sum)

        total = (n+1)*(n)/2

        missing = round(total - sum)
        return missing

f1 = Find_Missing()
print(f1.missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],11))


from turtle import right
from setuptools import find_namespace_packages



def duplicate(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return True

    return False

print(duplicate(array))


def findingMinMax(arr):
    mini = arr[0]
    maxi = arr[0]
    for i in range(len(arr)):
        mini = min(mini, arr[i])
        maxi = max(maxi, arr[i])

    return mini, maxi

print(findingMinMax(array))

####################################
############################################
###   Duplicate Zeros

arr = [1,0,2,3,0,4,5,0]
#Output: [1,0,0,2,3,0,0,4]
array = [1, 0, 2, 5]

class Solution:
  def duplicateZeros(self, arr):
    zeros = arr.count(0)
    i = len(arr) - 1 # 7
    j = len(arr) + zeros - 1  # 10

    while i < j:
      print(arr)
      if j < len(arr):
        print('here i am', arr[j],' , ', arr[i])
        arr[j] = arr[i]
      if arr[i] == 0:
        j -= 1
        if j < len(arr):
          arr[j] = arr[i]
      i -= 1
      j -= 1

    return arr

sol = Solution()
print(sol.duplicateZeros(arr))




def shiftRight(arr, n):
    for i in range(len(arr)-1, n, -1):
        arr[i] = arr[i-1]
    
    print('shift',arr)
    return arr

def duplicateZeroes(arr):
    print(arr)
    index = []
    for i in range(len(arr)):
        if arr[i] == 0:
            index.append(i)
    print(index)
    for i in range(len(index)):
        shiftRight(arr, index[i])
        arr[index[i]] = 0

    return arr

print(duplicateZeroes(arr))


def majorityElement(nums):
    n = len(nums)
    counter = 0
    for i in range(n):
        count = nums.count(nums[i])
        if count >= round(n/2):
            counter = max(counter, count)

    for i in range(n):
        if nums.count(nums[i]) == counter:
            return nums[i]
nums = [6,5,5]

def majorityElement(nums):       
    ans = None  # 6 5 5
    count = 0   # 1 0 1

    for num in nums:
        if count == 0:
            ans = num
        count += (1 if num == ans else -1)

    return ans

    
print(majorityElement(nums))

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

# class Solution:
#   def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#     if len(nums1) > len(nums2):
#       return self.intersect(nums2, nums1)

#     ans = []
#     count = Counter(nums1)

#     for num in nums2:
#       if count[num] > 0:
#         ans.append(num)
#         count[num] -= 1

#     return ans
    

# print(intersection(nums1, nums2))

def intersection(arr1, arr2):
    arr3 =[]
    for num in arr1:
        for nums in arr2:
            if num == nums:
                if(arr3.count(num) == 0):
                    arr3.append(num)

    return arr3
    

print(intersection(nums1, nums2))

def thirdMax(nums):
    third=[]
    if len(nums) < 3:
        return max(nums)
    else:
        while len(nums) > 0:
            maxim = max(nums)
            for i in range(nums.count(maxim)):
                if third.count(maxim) < 1:
                    third.append(maxim)
                nums.remove(maxim)

        if len(third) >=3:
            return third[2]

        else:
            return third[0]

print(thirdMax([1, 1, 2]))

def threesum(nums):
    if len(nums) < 3:
      return []

    ans = []

    nums.sort()

    for i in range(len(nums) - 2):
      if i > 0 and nums[i] == nums[i - 1]:
        continue
      l = i + 1
      r = len(nums) - 1
      while l < r:
        sum = nums[i] + nums[l] + nums[r]
        if sum == 0:
          ans.append([nums[i], nums[l], nums[r]])
          l += 1
          r -= 1
          while nums[l] == nums[l - 1] and l < r:
            l += 1
          while nums[r] == nums[r + 1] and l < r:
            r -= 1
        elif sum < 0:
          l += 1
        else:
          r -= 1

    return ans

print(threesum([-1,0,1,2,-1,-4]))


def assignCookies(g, s):
  given = 0
  i = len(g)-1
  j = len(s)-1
  while(i>=0 and j>=0):
    if(s[j] >= g[i]):
      given +=1
      i-=1
      j-=1
    else:
      i-=1

  return given

print(assignCookies([1, 2, 3], [1, 1]))

def ranking(score):
  sorted_array = sorted(score, reverse=True)
  answer = []
  answers = []
  for i in range(len(score)):
    for j in range(len(sorted_array)):
      if score[i] == sorted_array[j]:
        answer.append(f"{j+1}")

  for item in answer:
    if(item == '1'):
      item  = 'Gold Medal'
    elif(item =='2'):
      item = 'Silver Medal'
    elif(item == "3"):
      item = 'Bronze Medal'

    answers.append(item)
    
  return answers

print(ranking([10,3,8,9,4]))

# print([10,3,8,9,4])
# print(sorted([10,3,8,9,4], reverse=True))

def pair(array):
  array.sort()
  pairarray= []
  sum = 0
  for i in range(0, len(array), 2):
    pairarray.append((array[i], array[i+1]))
  print(array)

  for i in range(len(pairarray)):
    sum += pairarray[i][0]

  return sum

print(pair([6,2,6,5,1,2]))
from collections import Counter

def harmonius(nums):
  ans = 0
  count = Counter(nums)
  print(nums)
  print(count)

  for num, freq in count.items():
    print(num, freq)
    if num + 1 in count:
      print('num+1', num +1, 'count[num + 1]', count[num + 1])
      ans = max(ans, freq + count[num + 1])

  return ans
  nums.sort()
  answerArray = []
  answer = 0
  count = 0

  for i in range(len(nums)-1):
    if nums[i+1] - nums[i] <= 1 :
      answerArray.append(nums[i])
      count +=1
  answerArray.append(nums[count])

  print(nums)
  return answerArray

print(harmonius([1,3,2,2,5,2,3,7]))

import math
def maximumProduct(nums):
  mini = math.inf
  secondMin = math.inf
  maxi = -math.inf
  secondMax = -math.inf
  thirdMax = -math.inf

  for num in nums:
      if num <= mini:
        secondMin = mini
        mini = num
      elif num <= secondMin:
        secondMin = num

      if num >= maxi:
        thirdMax = secondMax
        secondMax = maxi
        maxi = num
      elif num >= secondMax:
        thirdMax = secondMax
        secondMax = num
      elif num >= thirdMax:
        thirdMax = num

  return max(mini * secondMin * maxi, maxi * secondMax * thirdMax)


print(maximumProduct([-100,-98,-1,2,3,4]))
import  bisect

def containRectangle(rectangles, points):
  ans = []
  yToXs = [[] for _ in range(101)]
  print(yToXs)

  for l, h in rectangles:
    yToXs[h].append(l)

  print(yToXs)

  for xs in yToXs:
    xs.sort()
  
  print(yToXs)

  for xi, yi in points:
    count = 0
    for y in range(yi, 101):
      xs = yToXs[y]
      count += len(xs) - bisect.bisect_left(xs, xi)
    ans.append(count)

  return ans

print(containRectangle([[1,8],[2,4],[3,1]], [[1,3],[1,1]]))


num = int(input("Enter the number: "))

def oddOrEven(val):
  ans = val%2
  switch = {
      0: "Even",
      1: "Odd",
  }
  return switch[ans]

print(oddOrEven(num))

arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]

def diagonal_difference(arr):
  for i in range(len(arr)):
    print(arr[i][i])

  for j in range(len(arr)):
    print(arr[j][abs(j-(len(arr[j])-1))])

diagonal_difference(arr)


def plusMinus(arr):
    # Write your code here
    n = len(arr)
    pos = 0
    neg = 0
    nut = 0
    for i in range(n):
        if arr[i] < 0:
            neg+= 1
        elif arr[i] > 0:
            pos+= 1
        else:
            nut +=1
    print(pos, neg, nut)
    return "{:.6f}".format(pos/n), "{:.6f}".format(neg/n), "{:.6f}".format(nut/n)

print(plusMinus([-4, 3, -9, 0, 4, 1]))

def minMax(arr):
  mini = 0
  maxi = 0
  arr.sort
  for i in range(len(arr)-1):
    mini += arr[i]

  for j in range(1, len(arr)):
    maxi += arr[j]

  return mini, maxi

print(minMax([7, 69, 2, 221, 8974]))

def candles(arr):
  maxi = arr[0]
  for i in range(len(arr) - 1):
    maxi = max(maxi, arr[i+1])
  num = arr.count(maxi)
  print(num, maxi)

candles([82, 49, 82, 82, 41, 82, 15, 63, 38, 25])

def pmConvertion(str):
  hour = int("".join((str[0], str[1])))
  if  hour>=1 and hour < 12:
    changed = hour + 12
  else:
    ar = []
    for i in str:
      ar.append(i)
    ar.pop()
    ar.pop()

    return ''.join(ar)
  arr = []
  for i in str:
    arr.append(i)
  if changed<10:
    arr[0] = '0'
    arr[1] = changed
  else:
    arr[0] = f"{changed//10}"
    arr[1] = f'{changed%10}'
  arr.pop()
  arr.pop()
  return ''.join(arr)

def amConvertion(str):
  hour = int("".join((str[0], str[1])))
  if  hour== 12:
    changed = 00
  else:
    ar = []
    for i in str:
      ar.append(i)
    ar.pop()
    ar.pop()
    return ''.join(ar)
  arr = []
  for i in str:
    arr.append(i)
  if changed<10:
    arr[0] = '0'
    arr[1] = f'{changed}'
  else:
    arr[0] = f"{changed//10}"
    arr[1] = f"{changed%10}"
  arr.pop()
  arr.pop()
  return ''.join(arr)

def timeConversion(string):
  if string[len(string) -2] == "P" or string[len(string) -2] == "p":
    return pmConvertion(string)
  else:
    return amConvertion(string)


print(timeConversion("12:01:00AM"))

def gradingStudents(grades):
  arr = []
  for item in grades:
    if item <= 33:
      arr.append(item)
      pass
    elif (item+1) % 5 != 0 and item+2 % 5 !=0 and item + 3 != 0:
      arr.append(item)
    else:
      num = item
      for i in range(2):
        num+=1
        if num % 5 == 0:
          arr.append(num)
          pass
      # arr.append(item)  

  for item in grades:
    num = item
    for i in range(3):
      if num % 5 != 0:
        num+=1

    if item < 33:
      arr.append(item)
    elif num - item < 3:
      arr.append(num)
    elif num - item == 3:
      arr.append(item)      
  return arr

print(gradingStudents([22,
86,
30,
0,
16,
51,
53,
42,
48,
22,
69,
12,
27,
34,
24,
95,
16,
32,
22,
52,
56,
71,
95]))

