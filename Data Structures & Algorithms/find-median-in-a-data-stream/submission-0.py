import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = [] # left
        self.min_heap = [] # right

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            heapq.heappush(self.max_heap, -num)
        else:
            left_max = -self.max_heap[0]
            if num <= left_max:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
        # left is too big, pop and move to right
        if len(self.max_heap) == len(self.min_heap) + 2:
            val = -heapq.heappop(self.max_heap)      
            heapq.heappush(self.min_heap, val)
        
        if len(self.min_heap) == len(self.max_heap) + 2:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            first = -self.max_heap[0]
            second = self.min_heap[0]
            return (first + second) / 2
        
        if len(self.max_heap) == len(self.min_heap) + 1:
            mid = -self.max_heap[0]
            return mid
        
        if len(self.min_heap) == len(self.max_heap) + 1:
            mid = self.min_heap[0]
            return mid
        
        