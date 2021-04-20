# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        if not root:
            return []

        def get_depth(root):
            if root is None:
                return -1
            return max(get_depth(root.left), get_depth(root.right)) + 1
        
        n = get_depth(root) # 获得深度
        res = [['']*((1<<(n+1))-1) for i in range(n+1)]

        # 前序遍历
        def fill(root, d, l, r): # l r 为 以 root 为 根节点的子树覆盖范围
            if root is None:
                return
            mid = (l+r)//2
            res[d][mid] = str(root.val)

            fill(root.left, d+1,  l, mid - 1)
            fill(root.right, d+1,  mid+1, r)
        
        fill(root, 0, 0, (1<<n+1) - 2)
        return res

