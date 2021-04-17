# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:

        self.record = collections.defaultdict(int) # 记录子树和的次数
        self.max_time = 0 #记录最大次数
        self.ans = [] # 记录遍历过程中最大次数的案例
        # 后序遍历
        def dfs(root):
            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            tmp = left + right + root.val
             
            self.record[tmp] += 1 # tmp 的次数加1
            if self.record[tmp] == self.max_time:
                self.ans.append(tmp)
            if self.record[tmp] > self.max_time:
                self.max_time = self.record[tmp]
                self.ans = [tmp]
            
            return tmp
        
        dfs(root)
        return self.ans