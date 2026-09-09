class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path, res = [], []
        
        def backtrack(index, total):
            # base case
            if total == target:
                res.append(path.copy())
                return
            if total > target:
                return
            if index == len(nums):
                return
            
            path.append(nums[index])
            backtrack(index, total + nums[index])
            path.pop()

            backtrack(index + 1, total)
        
        backtrack(0, 0)
        return res