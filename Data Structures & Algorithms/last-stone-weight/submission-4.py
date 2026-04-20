class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap,-i)
        while(len(heap)>=2):
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if(x>y):
                heapq.heappush(heap, -(x-y))
        heapq.heappush(heap,0)
        return abs(heap[0])