import heapq
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        maxc = 0
        res = 0
        for i in nums:
            freq[i] = freq.get(i,0)+1
            if(maxc<freq[i]):
                maxc=freq[i]
                res=i
        return res