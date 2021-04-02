# 所有

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def bt(root):
            if root is None:
                return root

            left = bt(root.right)
            right = bt(root.left)
            # 后序遍历
            root.left = left
            root.right = right
            return root
        
        return bt(root)