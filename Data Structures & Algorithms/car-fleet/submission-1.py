class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True) # sort by position descending
        
        stack = []
        for p, s in cars:
            time = (target - p) / s
            stack.append(time)

            # if the current car arrive faster or same time as the car 
            # ahead, we merget two into one, these two car become fleet(or one group)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # pop the current, which leave car ahead and become one
        
        return len(stack)