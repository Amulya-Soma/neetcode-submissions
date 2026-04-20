class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,a in enumerate(nums):
            if i>0 and nums[i-1]==a:
                continue
            b = i+1
            c = len(nums)-1
            while b<c:
                if(a+nums[b]+nums[c]>0):
                    c-=1
                elif (a+nums[b]+nums[c]<0):
                    b+=1
                else:
                    res.append([a,nums[b],nums[c]])
                    b+=1
                    while b<c and nums[b]==nums[b-1]:
                        b+=1
        return res