class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = defaultdict(int)
        for i,n in enumerate(nums):
            val = target - n
            if val in prev_map:
                return [prev_map[val],i]
            prev_map[n] = i