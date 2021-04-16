# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 二叉树如果根节点为 i， [start, i] 为 左子树的区间范围 [i+1, end]为右子树的区间范围 
    def generateTrees(self, n: int) -> List[TreeNode]:

        # 返回取值范围 为 [start, end] 范围之内的所有可能搜索二叉树
        def gentree(start, end):
            if start > end: # 如果是不规范的缩影，返回  None
                return [None,]
            
            ans = []
            for i in range(start, end+1): # 从 [start， end+1]中挑选出一个作为根节点
                for l in gentree(start, i-1): # 左子树区间为[start, i-1]， l遍历所有在该区间的可能子树形式
                    for r in gentree(i+1, end): # 
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        ans.append(node)
            
            return ans
        
        return gentree(1, n) if n else []
        