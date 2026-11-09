class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if total > target or i == len(candidates):
                return
            
            # take a number
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])
            # skip a number
            cur.pop()


            # skip duplicate
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)

        return res