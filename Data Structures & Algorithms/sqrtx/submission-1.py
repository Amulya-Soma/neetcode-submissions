class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = 0
        while(l<=r):
            mid = l+((r-l)//2)
            if(mid*mid==x):
                return mid
            elif(mid*mid>x):
                r = mid-1
            elif(mid*mid<x):
                l = mid+1
                res = mid
        return res

# 0123456789
# 0+9//2 = 4
# 0+5//2 = 3
# 0+4//2 = 2