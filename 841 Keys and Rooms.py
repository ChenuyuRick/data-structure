class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        rooms_status = [False]*len(rooms)
        rooms_status[0] = True
        stack = [0]
        while stack:
            node = stack.pop()
            for nei in rooms[node]:
                if not rooms_status[nei]:
                    rooms_status[nei] = True
                    stack.append(nei)
        return all(rooms_status)   
