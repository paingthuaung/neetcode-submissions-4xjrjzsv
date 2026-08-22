import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = []
        count = {}
        for t in tasks:
            count[t] = count.get(t,0)+1
        
        for task, count in count.items():
            heapq.heappush(max_heap, (-count, task, None))
        time = 0
        cooldown = deque()
        while max_heap or cooldown:
            time += 1

            while cooldown and cooldown[0][2] <= time:
                remain_count, task, _ = cooldown.popleft()
                heapq.heappush(max_heap, (remain_count, task, None))

            if max_heap:
                remain_count, task, _ = heapq.heappop(max_heap)
                remain_count = remain_count + 1
                available_time = time + n + 1
                if remain_count:
                    cooldown.append((remain_count,task,available_time))
        return time
            
        
            