# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # 返回前序遍历的结果，对空节点也进行特殊编码
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '#'
        
        return str(root.val) + ',' + self.serialize(root.left) + ','+ self.serialize(root.right)
        

    # 单靠前序遍历的还原
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        ans = data.split(',')
        if ans[0] == '#':
            return None

        start = 0
        def dfs():
            nonlocal start
  
            if ans[start] == '#':
                start += 1
                return None
            
            
            root = TreeNode(int(ans[start]))
            start += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()
        
        


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))