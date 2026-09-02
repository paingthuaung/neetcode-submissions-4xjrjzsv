import heapq
class MedianFinder:

    def __init__(self):
        # create two heap, one for small num, and one for large
        self.max_heap = [] # left
        self.min_heap = [] # right

    def addNum(self, num: int) -> None:
        # if heap empyt, add to left heap
        if not self.max_heap:
            heapq.heappush(self.max_heap, -num)
        else:
            # if num is less than left, put it in left
            # else put into right
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
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        # eg [1,2,3] and [4,5] mid is 3
        if len(self.max_heap) == len(self.min_heap) + 1:
            return -self.max_heap[0] 
        
        if len(self.min_heap) == len(self.max_heap) + 1:
            return self.min_heap[0]
        
        