import heapq
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        print(freq)
        heap = []
        for f in freq.keys():
            heapq.heappush(heap,(-freq[f],f))
        print(heap)
        return heapq.heappop(heap)[1]