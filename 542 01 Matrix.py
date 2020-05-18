class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # Initialization
        R = len(matrix)
        C = len(matrix[0])
        distance = []
        queue = []
        for i in range(R):
            distance.append([None]*C)
        
        # Scan the matrix to get 0
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    distance[i][j] = 0
                    if i > 0 and distance[i - 1][j] is None:
                        distance[i - 1][j] = 1
                        queue.append((i - 1, j))
                    if j > 0 and distance[i][j - 1] is None:
                        distance[i][j - 1] = 1
                        queue.append((i, j - 1))
                else:
                    if (i > 0 and matrix[i - 1][j] == 0) or (j > 0 and matrix[i][j - 1] == 0):
                        distance[i][j] = 1
                        queue.append((i, j))
        
        # Fill in other places
        while queue:
            row, col = queue.pop(0)
            value = distance[row][col] + 1
            if row > 0 and distance[row - 1][col] is None:
                distance[row - 1][col] = value
                queue.append((row - 1, col))
            if col > 0 and distance[row][col - 1] is None:
                distance[row][col - 1] = value
                queue.append((row, col - 1))
            if row < R-1 and distance[row + 1][col] is None:
                distance[row + 1][col] = value
                queue.append((row + 1, col))
            if col < C-1 and distance[row][col + 1] is None:
                distance[row][col + 1] = value
                queue.append((row, col + 1))
        return distance
