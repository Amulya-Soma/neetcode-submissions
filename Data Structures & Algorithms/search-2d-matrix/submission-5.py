class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        print(ROWS,COLS)
        top_row = 0
        bottom_row = ROWS-1
        while(top_row<=bottom_row):
            mid_row = (top_row+bottom_row)//2
            if(target<matrix[mid_row][0]):
                bottom_row = mid_row-1
            elif(target>matrix[mid_row][-1]):
                top_row = mid_row+1
            else:
                break
        # if top_row>bottom_row:
        #     return False
        left = 0
        right = COLS-1
        while(left<=right):
            mid = (left+right)//2
            if(target<matrix[mid_row][mid]):
                right = mid-1
            elif(target>matrix[mid_row][mid]):
                left = mid+1
            elif(target == matrix[mid_row][mid]):
                return True
        return False