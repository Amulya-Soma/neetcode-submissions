class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicty1 = {}
        for i in range(len(nums)):
            dicty1[i] = target-nums[i]
            if(dicty1[i] in nums):
                k = nums.index(dicty1[i])
                if(i!=k):
                    return [min(i,k),max(i,k)]
