"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    #BFS
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return
        import collections
        q = collections.deque([root])
        res  = []
        while q:
            ans = []
            sz = len(q)
            for _ in range(sz):
                top = q.popleft()
                ans.append(top.val)
                # 可以简写 为 
                q.extend(top.children)
                # for i in top.children:
                #     if i:
                #         q.append(i)
        
            res.append(ans)
        
        return res

    # dfs 前序遍历
    results = []
    def dfs(root, level):
        if len(results) == level:
            results.append([])
        results[level].append(root)

        for i in root.children:
            dfs(i, level+1)
    
    dfs(root, 0)
    return results
