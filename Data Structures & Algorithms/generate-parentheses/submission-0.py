class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(cur,close, open):
            if len(cur) == 2 * n:
                res.append(cur)
                return
            if open < n:
                backtrack(cur + '(',close, open + 1)
            if close < open:
                backtrack(cur + ')', close + 1, open)                
        
        backtrack("", 0, 0)
        return res
        