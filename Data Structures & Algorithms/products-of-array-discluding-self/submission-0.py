class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right, result = [1] * n, [1] * n, [1] * n

        # populate the left array
        # we start at index 1 because we know first element will always 1
        # because there is no element before that, same with right
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        
        # populate the right array
        # n-2 mean second last element, -1 mean loop will end in index 0
        # and last -1 mean downward step by 1
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # calculate result
        for i in range(n):
            result[i] = left[i] * right[i]
        
        return result
            
            
        