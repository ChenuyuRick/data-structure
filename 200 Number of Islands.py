class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
    
    def isValid(self, grid, row, col):
        n_rows = len(grid)
        n_cols = len(grid[0])
        if 0 <= row < n_rows and 0 <= col < n_cols:
            return True
        return False
    
    def dfs(self, grid, row, col):
        grid[row][col] = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for d in directions:
            rn, cn = row + d[0], col + d[1]
            if self.isValid(grid, rn, cn) and grid[rn][cn] == '1':
                self.dfs(grid, rn, cn)
        
