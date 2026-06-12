class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        for current_index, current_temp in enumerate(temperatures):
            # if current temp is greater than temp on top of stack
            while stack and current_temp > temperatures[stack[-1]]:
                pop_index = stack.pop()
                result[pop_index] = current_index - pop_index
            
            stack.append(current_index)
        
        return result