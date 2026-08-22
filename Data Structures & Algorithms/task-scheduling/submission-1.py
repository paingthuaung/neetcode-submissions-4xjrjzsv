import heapq
from collections import deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. Count frequencies
        freq_map = {}
        for t in tasks:
            freq_map[t] = freq_map.get(t, 0) + 1
        
        # 2. Build Max-Heap using negative counts
        max_heap = []
        for task, cnt in freq_map.items():
            heapq.heappush(max_heap, (-cnt, task))
            
        time = 0
        cooldown = deque()  # Stores pairs: (remaining_count, available_time)
        
        while max_heap or cooldown:
            time += 1

            # 3. Process the task for the current time slice
            if max_heap:
                neg_count, task = heapq.heappop(max_heap)
                remain_count = neg_count + 1  # Reduce absolute frequency by 1
                
                if remain_count < 0:
                    available_time = time + n
                    cooldown.append((remain_count, available_time))
            
            # 4. Check if any cooling task is ready for the NEXT time slice
            while  cooldown and cooldown[0][1] <= time:
                rem_cnt, _ = cooldown.popleft()
                # Re-insert with a dummy task name or just the frequency count
                heapq.heappush(max_heap, (rem_cnt, "dummy"))
                
        return time

            
        
            