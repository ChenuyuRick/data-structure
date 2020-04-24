class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    before = 0
                elif i == 0:
                    before = grid[0][j-1]
                elif j == 0:
                    before = grid[i-1][0]
                else:
                    before = min(grid[i-1][j], grid[i][j-1])
                grid[i][j] = before + grid[i][j]
        
        return grid[rows-1][cols-1]
