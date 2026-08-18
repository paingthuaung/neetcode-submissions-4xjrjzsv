import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for p in points:
            # origin is zero, not necessary to include
            # we don't need sqrt because it is still the same without
            # sqrt, removing sqrt save some computation
            distance = (p[0])**2 + (p[1])**2
            heapq.heappush(max_heap, (-distance, p))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        res = []
        while max_heap:
            _, val = heapq.heappop(max_heap)
            res.append(val)

        return res 

    