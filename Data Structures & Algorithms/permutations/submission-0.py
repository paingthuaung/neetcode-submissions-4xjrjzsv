class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        track_list = [False] * len(nums)

        def dfs(cur):
            
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            # iterate all numbers
            for i in range(len(nums)):
                
                # if a number being used
                if track_list[i] == True:
                    continue
                
                # add number
                cur.append(nums[i])
                #print(cur)
                track_list[i] = True

                dfs(cur)

                # undo number
                cur.pop()
                track_list[i] = False

        dfs([])
        return res


        