import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap,-i)
        print(heap)
        while(len(heap)>1):
            a=-heapq.heappop(heap)
            b=-heapq.heappop(heap)
            if(a>b):
                heapq.heappush(heap,-(a-b))
        heap.append(0)
        return abs(heap[0])