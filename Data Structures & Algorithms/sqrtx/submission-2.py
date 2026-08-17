class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while(left<=right):
            mid = (left+right)//2
            val = mid*mid
            if(val==x):
                return mid
            elif(val<x):
                left=mid+1
                res = mid
            elif(val>x):
                right = mid-1
        return res