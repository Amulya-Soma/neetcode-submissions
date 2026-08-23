class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dicty = {}
        for i,val in enumerate(nums):
            diff = target-val
            if diff in dicty:
                return [dicty[diff],i]
            dicty[val] = i