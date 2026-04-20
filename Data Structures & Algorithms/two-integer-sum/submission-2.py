class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicty1 = {}
        for i in range(len(nums)):
            dicty1[i] = target-nums[i]
            print(dicty1)
            if(dicty1[i] in nums):
                print(nums.index(dicty1[i]))
                j = nums.index(dicty1[i])
                if(i!=j):
                    return [min(i,j),max(i,j)]