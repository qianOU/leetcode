# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 后序遍历
    # 遍历了两次， 后序可以优化成一次DFS 
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        self.max_d = -1
        self.record = []
        def dfs(root, max_d):
            if root is None:
                return 
            if root.left is None and root.right is None:
                if self.max_d < max_d:
                    self.max_d = max_d
                    self.record = [root]
                elif self.max_d == max_d:
                    self.record.append(root)
            
            dfs(root.left, max_d+1)
            dfs(root.right, max_d+1)

        dfs(root, 0)
        if len(self.record) == 1:
            return self.record[0]
        
        def lastnode(root):
            if root is None:
                return
            if root.val in [i.val for i in self.record]:
                return root
            
            left = lastnode(root.left)
            right = lastnode(root.right)

            if left is not None and right is not None:
                    return root
            if left:
                return left
            elif right:
                return right
            return 

        return lastnode(root)

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        # dfs 用于返回 以 root 为 根节点的子树深度，以及 最深节点的最近祖先
        # 
        def dfs(root):
            if root is None:
                return 0, None 
            l_d, lans = dfs(root.left)
            r_d, rans = dfs(root.right)
            # 如果左子树的深度 == 右子树的深度， 返回当前节点
            # PS： 此题有效的原因是 题目中隐含了 最深节点的公共节点唯一的条件
            if l_d == r_d:
                return l_d + 1, root
            if l_d > r_d: # 如果左子树的深度 大于 右子树的深度, 则 最深节点的最近祖先 一定位于左子树中
                return l_d+1, lans
            if r_d > l_d:
                return r_d+1, rans
        
        return dfs(root)[1]

# 由层次遍历，还原一棵二叉树
def back_tree(nums = [1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1]):
    root =  TreeNode(nums.pop(0))
    queue = []
    queue.append(root)

    while len(queue) and len(nums):
       q = queue.pop(0)
       if q is None:
           continue
       q.left = TreeNode(nums.pop(0)) if nums[0] is not None else nums.pop(0) # 如果是 None 叶修要弹出
       q.right = TreeNode(nums.pop(0)) if nums[0] is not None else nums.pop(0)
       queue.append(q.left)
       queue.append(q.right)
    #    print(queue)

    return root


root = back_tree([3,5,1,6,2,0,4])
a = Solution().lcaDeepestLeaves(root)
print(a.val)