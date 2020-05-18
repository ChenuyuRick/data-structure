class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if len(image) == 0 or len(image[0]) == 0:
            return image
        OrgColor = image[sr][sc]
        if OrgColor == newColor: return image
        R = len(image)
        C = len(image[0])
    
        def dfs(row, col):
            if image[row][col] == OrgColor:
                image[row][col] = newColor
                if row + 1 < R: dfs(row + 1, col)
                if row - 1 >= 0: dfs(row - 1, col)
                if col + 1 < C: dfs(row, col + 1)
                if col - 1 >= 0: dfs(row, col - 1)
        
        dfs(sr, sc)
        return image
