class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicty = {}
        for idx, val in enumerate(nums):
            diff = target-val
            if diff in dicty:
                return [dicty[diff],idx]
            dicty[val] = idx
        print(dicty)