# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if root is None:
            return 

        ans = []
        # 自底向下 后序遍历
        # 递归拆分符合条件的节点
        def dfs(root):
            if root is None:
                return

            left = dfs(root.left)
            right = dfs(root.right)
            # 主要为了应对连续需要拆分的元素情况
            root.left = left # 更新拆分的情况
            root.right = right

            if root.val in to_delete:
                if root.left: # 如果 root 被拆分则左右子树分别加入结果集中
                    ans.append(root.left)
                    
                if root.right:
                    ans.append(root.right)
                     
                return None # root 节点被拆分，所以需要返回 None 给父节点
            
            
            return root # 对于正常的点，返回 root即可
        # 创建一个虚假节点指向头节点，主要为了处理头节点需要被删除的情况
        dumy = TreeNode(None)
        dumy.left = root 
        
        dfs(dumy)
        if dumy.left: # 如果 头节点没被删除的话， 需要将头节点加入结果集，作为选项之一
            ans.append(dumy.left)
        
        
        return ans

