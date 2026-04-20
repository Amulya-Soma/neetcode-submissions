import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heapq.heappush(heap,-i)
        print(heap)
        for _ in range(k):
            a = -heapq.heappop(heap)
        return a
        