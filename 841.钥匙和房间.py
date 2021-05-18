class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        
        def dfs(id_r, path, visited):
            if all(path):
                return True
            
            for key in rooms[id_r]:
                if key in visited:
                    continue
                path[key] = True
                visited.add(key)
                if dfs(key, path, visited):
                    return True
                
               
        
        n = len(rooms)
        path = [True]
        path.extend(False for i in range(n-1))

        return dfs(0, path, set([0])) is not None

