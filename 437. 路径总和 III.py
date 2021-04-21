# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        
        self.count = 0
        # 方法一： 纯 dfs 效率较低， 可以使用前缀和来减少运算
        # 返回 以 root 为根节点的 路径数值和 list
        #  后序遍历
        def dfs(root) -> list:
            if root is None:
                return [0]
            
            
            left = dfs(root.left)
            right = dfs(root.right)

            for i in left:
                if i == targetSum - root.val:
                    self.count += 1
                ans.append(i+root.val)
            
            for i in right:
                if i == targetSum - root.val:
                    self.count += 1
                ans.append(i+root.val)
            
            return ans
        
        # dfs(root)
        # return self.count


        # 方法二： 前缀和 + 前序遍历

        def pathSum(self, root: TreeNode, targetSum: int) -> int:
            
            records = {0: 1}
            # 前序遍历 + 前缀和记录字典 + 状态恢复
            def prefix(root, sum):
                res = 0 # 记录符合条件的路径数量
                if root is None:
                    return
                
                cur = sum + root.val
                records[cur] = records.get(cur, 0) + 1 # 更新状态记录字典
                res += records.get(cur - targetSum, 0)

                left = prefix(root.left, cur)
                right = prefix(root.right, cur)

                res += left + right

                records[cur] = records.get(cur) - 1 # 状态恢复，即在遍历完一个节点的所有子节点后，将其从map中除去。
                return res
        
            reutrn prefix(root, 0)
