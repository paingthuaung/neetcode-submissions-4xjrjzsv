class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(cur,i):
            if i >= len(nums):
                res.append(cur.copy())
                return
            # add number
            cur.append(nums[i])
            backtrack(cur,i+1)
            cur.pop()
            # skip duplicate
            while i + 1 < len(nums) and nums[i] == nums[i + 1]: 
                i += 1
            backtrack(cur, i+1)
        backtrack([],0)
        return res
            

        
        