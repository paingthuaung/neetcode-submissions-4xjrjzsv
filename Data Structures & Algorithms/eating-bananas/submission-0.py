import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2
            # it take p/k(k is mid), to finish x pile at k rate
            # math ceil a math function that always rounds 
            # a number UP to the nearest whole integer, like 2.1 to 3, 3.2 to 4
            total_hour = sum(math.ceil(p/mid) for p in piles)
            # if total hour is less than h, we find lower than that 
            # we need minimun hour to finish
            if total_hour <= h:
                high = mid - 1
            else:
                # if it too slow, we need to increase 
                low = mid + 1
        
        return low
        