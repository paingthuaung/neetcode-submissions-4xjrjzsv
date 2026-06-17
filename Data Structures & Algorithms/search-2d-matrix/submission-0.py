class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        # flatten 2d array into 1D, since they already sorted,
        # we can just use binary search on 1D array
        start, end = 0, (rows * cols) - 1

        while start <= end:
            mid = (start + end) // 2
            # convert  convert a single index (from a 1D array) 
            # back into row and column coordinates (for a 2D matrix).
            # let say index is 9, row calculation-> how many row can 9 fit
            # it is 9 % 4 == 2, so it is row 2, and column calculation
            # how many left over after filling those rows, 9 % 4 remainder is 1
            # it is col 1, so it is (2, 1)
            element = matrix[mid // cols][mid % cols]

            if target == element:
                return True
            elif target > element:
                start = mid + 1
            else:
                end = mid - 1
    
        return False
                
        