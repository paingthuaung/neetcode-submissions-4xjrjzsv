class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # if mid is greater than right, min is on the righ part
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid # if not, min is under mid, because array are sort
         #  When l == r, they point to the minimum element   
        return nums[l]

        