import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # dictionary, heap, queue
        freq = defaultdict(int)
        heap = []
        for i in tasks:
            freq[i] = freq.get(i,0)+1
        for i in freq.values():
            heapq.heappush(heap,-i)
        time = 0
        q = deque()
        while heap or q:
            time+=1
            if heap:
                ele = 1+heapq.heappop(heap)
                if ele:
                    q.append([ele,time+n])
            if q and q[0][1]==time:
                heapq.heappush(heap,q.popleft()[0])
        return time