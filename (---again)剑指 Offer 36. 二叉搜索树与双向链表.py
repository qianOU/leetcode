"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    # 中序遍历
    # 巧妙： 使用全局变量来记录，头节点，以及 先前节点，这就保证了 每一次遍历到当前节点时，先前节点都是符合要求的中序遍历的结果
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None: return 
        # 使用全局变量来记录，头节点，以及 先前节点
        head, pre = None, None

        def dfs(cur):
            nonlocal head, pre
            if cur is None: return

            dfs(cur.left)
            
            if pre: # 如果有先前节点则 构建关系
                pre.right, cur.left = cur, pre
            else: # 头节点
                head = cur
            
            # 更新先前节点
            pre = cur

            dfs(cur.right)
        
        dfs(root)
        head.left, pre.right = pre, head
        return head