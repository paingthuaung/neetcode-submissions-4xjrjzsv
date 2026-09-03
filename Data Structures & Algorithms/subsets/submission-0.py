class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        def backtrack(index):
            if index == len(nums):
                res.append(path.copy())
                return
            
            path.append(nums[index])
            backtrack(index + 1)
            path.pop()

            backtrack(index + 1)
        
        backtrack(0)
        return res

        