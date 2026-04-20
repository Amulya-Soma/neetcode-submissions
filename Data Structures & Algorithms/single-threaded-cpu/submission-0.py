class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort(key = lambda x:x[0])
        print(tasks)
        i = 0 # Current task
        time = tasks[0][0] #First enque value will be initial time we start from
        heap = [] #Min heap, pop gives smallest element
        result = []
        while heap or i<len(tasks): #while there are still values in heap or while there are still tasks
            while i<len(tasks) and tasks[i][0]<=time:
                heapq.heappush(heap,[tasks[i][1], tasks[i][2]])
                i+=1
            if not heap:
                time = tasks[i][0] #The previous task is just done, this is the new task's latest enque time
            else:
                process_time,idx=heapq.heappop(heap)
                time = time+process_time #Add the process time taken to complete this task to original time.
                result.append(idx)
        return result