# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode):
        from collections import defaultdict
        if root is None:
            return []
        
        def get_range(root):
            
            q = [(root, 0)]
            left = float('inf')
            right = float('-inf')
            while q:
                node, col = q.pop(0)
                if col < left:
                    left = col
                if right < col:
                    right = col

                if node.left:
                    q.append((node.left, col-1))
                    
                if node.right:
                    q.append((node.right, col+1))


            
            return left, right

        left, right = get_range(root)
        # print(left, right)
        start = -1*left
        q = [(root, 0)]

        res = [[] for i in range(-1*left+right+1)] # 构建大表格
        
        
        while q:
            sz = len(q)
            records = defaultdict(list)
            for _ in range(sz):
                node, col = q.pop(0)
                records[start+col].append(node.val)
  
                if node.left:
                    q.append((node.left, col-1))
                    
                if node.right:
                    q.append((node.right, col+1))
                
            
            for key in records:
                res[key].extend(sorted(records[key]))
        
        return res