"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if node is None:
            return 

        # 记忆 旧节点 与 新节点之间的映射

        map_ = {}

        def dfs(a):
            if a is None:
                return Node(1)
            v = a.val
            one = Node(v)
            map_[a.val] = one
            ans = []
            for i in a.neighbors:
                if i.val not in map_: # 如果是 还么遇见过的旧节点，进行深拷贝
                    ans.append(dfs(i))
                else: # 如果是已经遇见过的旧节点，则进行 关系的绑定
                    ans.append(map_[i.val])

            one.neighbors = ans
            return one
        
       
        return dfs(node)