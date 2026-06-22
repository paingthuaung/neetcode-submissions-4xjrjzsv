class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            # check if left half is sorted
            if nums[l] <= nums[mid]:
                # if target between left and mid
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1 # right is mid - 1, mid is already check,mid cannot be target
                else:
                    l = mid + 1 # no include, it must be greater than mid
            # if right half is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1

            