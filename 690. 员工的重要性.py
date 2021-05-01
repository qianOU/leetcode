"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        records = {}
        items = {}

        for i in employees:
            imp = i.importance
            outers = i.subordinates
            records[i.id] = imp
            items[i.id] = outers
        
        from functools import lru_cache

        @lru_cache(None)
        def dfs(id):
            return records[id] + sum(dfs(i) for i in items[id])
        
        return dfs(id)