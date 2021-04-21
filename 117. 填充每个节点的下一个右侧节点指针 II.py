"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    # 前序遍历
    def connect(self, root: 'Node') -> 'Node':
        
        # 生成器 产出 合适的 next 节点
        def gen_next(root):
            root = root.next
            while root:
                
                if root.left:
                    cur_node = yield  root.left
                if root.right:
                    cur_node = yield root.right

                root = root.next
            
            yield None
                


        def dfs(root):
            if root is None:
                return 
            
            # 构建合适的下一个 next 节点的 生成器
            generator = gen_next(root)
            if root.left:
                if root.right:
                    root.left.next = root.right
                else:   
                    root.left.next = next(generator)

            if root.right and root.next:
                
                root.right.next = next(generator)
            
            # 要点
            # 因为使用的先序遍历，所以需要先将同一层的尾部链接好，这样子才能确保每次搜寻的是同一层完整的链路
            # 因此 需要先遍历 右子树 将 同一层的尾部链路构建好
            dfs(root.right) 
            dfs(root.left)
           
        
        dfs(root)
        return root
        
