class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num in enumerate(nums):
            val = target-num
            if(val in nums and nums.index(val)!=i):
                return [min(i,nums.index(val)),max(i,nums.index(val))]