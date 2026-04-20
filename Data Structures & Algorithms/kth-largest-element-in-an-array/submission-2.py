class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heapq.heappush(heap,-i)
        for _ in range(k):
            val = -heapq.heappop(heap)
        return val