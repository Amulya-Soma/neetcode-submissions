class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        result = []
        for i in points:
            dist = math.sqrt((i[0]*i[0])+(i[1]*i[1]))
            heapq.heappush(minheap,(dist,i))
        for _ in range(k):
            result.append(heapq.heappop(minheap)[1])
        return result
        