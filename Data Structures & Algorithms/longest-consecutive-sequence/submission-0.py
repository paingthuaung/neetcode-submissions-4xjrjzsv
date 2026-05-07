class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        longest = 0
        for n in num_set:
            # only start count if there is no  N - 1 value, 
            # which mean N is the beginning of list
            if (n - 1) not in num_set:
                current_num = n
                current_streak = 1

                while(current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
            
                longest = max(longest, current_streak)
    
        return longest

