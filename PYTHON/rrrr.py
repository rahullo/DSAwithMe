n = 51
bad = 10

def isBadVersion(int):
    if int == bad:
        return True
    else:
        return False

def firstBadVersion( n):
        ans = False
        while ans == False:
            if isBadVersion(n) == True:
                ans = True
                return n
            else:
                n-=1

print(firstBadVersion(n))