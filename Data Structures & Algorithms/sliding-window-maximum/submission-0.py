from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        for i in range(len(nums)):
            # check index in out of bound from current window
            # i - k + 1 calculates the absolute lowest valid index 
            # allowed in your current sliding window.
            if q and q[0] < i - k + 1: 
                q.popleft()
            # check if last item in que in lass than current incoming item
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            q.append(i)

            # wait for window ready, we cannot find max until 
            # we reach full window, which is k
            if i >= k - 1:
                result.append(nums[q[0]]) # que always store biggest item in the first index
        
        return result
        