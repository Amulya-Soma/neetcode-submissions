class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = defaultdict(int)
        for i,n in enumerate(nums):
            val_diff = target - n
            if(val_diff in prev_map):
                return [prev_map[val_diff],i]
            prev_map[n] = i