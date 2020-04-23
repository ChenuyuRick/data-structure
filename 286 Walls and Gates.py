class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        
        wall = -1
        gate = 0
        unknown = 2147483647
        
        current_level = []
        n_rows = len(rooms)
        n_cols = len(rooms[0])
        for i in range(n_rows):
            for j in range(n_cols):
                if rooms[i][j] == gate:
                    current_level.append((i, j))
        
        while current_level:
            next_level = []
            for i, j in current_level:
                distance = rooms[i][j]
                
                for next_i, next_j in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                    if 0 <= next_i < n_rows and 0 <= next_j < n_cols and rooms[next_i][next_j] == unknown:
                        rooms[next_i][next_j] = distance + 1
                        next_level.append((next_i, next_j))
            current_level = next_level
        
