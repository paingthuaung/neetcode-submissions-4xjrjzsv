import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.input = nums
        self.size = k
        heapq.heapify(self.input)
        while len(self.input) > k:
            heapq.heappop(self.input)  

    def add(self, val: int) -> int:
        heapq.heappush(self.input, val)
        if len(self.input) > self.size :
            heapq.heappop(self.input)
        
        return self.input[0]
