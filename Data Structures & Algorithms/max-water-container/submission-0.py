class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers at the beginning and end of the array
        left = 0
        right = len(height) - 1
        max_area = 0
      
        # Use two-pointer approach to find the maximum area
        while left < right:
            # Calculate the area with current left and right boundaries
            # Area = width * height (where height is the minimum of the two sides)
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
          
            # Update maximum area if current area is larger
            max_area = max(max_area, current_area)
          
            # Move the pointer pointing to the shorter line
            # This is optimal because moving the taller line would never increase the area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
      
        return max_area
        