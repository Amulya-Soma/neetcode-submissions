import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = []
        for i in nums:
            freq[i] = freq.get(i,0)+1
        print(freq)
        for i in freq.keys():
            heapq.heappush(heap,(freq[i],i))
            if(len(heap)>k):
                heapq.heappop(heap)
        result = []
        print(heap)
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        print(result)
        return result