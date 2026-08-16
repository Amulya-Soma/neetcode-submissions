class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        for i in range(0,len(nums)):
            mid = (low+high)//2
            if (target<nums[mid]):
                high = mid-1
            elif (target>nums[mid]):
                low = mid+1
            elif (target == nums[mid]):
                return mid
        return -1
