class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for i in nums:
            freq[i] = freq.get(i,0)+1
        print(freq)
        heap = []
        for i in freq.keys():
            heapq.heappush(heap,(freq[i],i))
            if(len(heap)>k):
                heapq.heappop(heap)
        print(heap)
        for _ in range(k):
            freq,ele=(heapq.heappop(heap))
            res.append(ele)
        return res