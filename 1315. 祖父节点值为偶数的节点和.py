
class Solution:
    # DFS
    # DFS 的每次迭代状态 也可以使用 三元组表示： （grand, parent, node）为函数参数
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sum = 0
        # 构建的 dfs 是直接联系当前节点 和 祖父节点的关系，所以是跨层遍历
        def dfs(root, grand=None):
            if root is None:
                return 0
            
            if grand and grand.val %2 == 0:
                self.sum += root.val
            if root.left is not None:
                dfs(root.left.left, root)
                dfs(root.left.right, root)
            if root.right is not None:
                dfs(root.right.left, root)
                dfs(root.right.right, root)
        
        # 遍历整棵树
        dfs(root) # 遍历 1-3-5-7.。。
        dfs(root.left) # 左子树遍历 2-4-6-8-。。
        dfs(root.right) # 右子树遍历 2-4-6-8-。。

        return self.sum

    
    # BFS 
    # 如果当前节点是偶数，则将其所有 孙子 节点 的值累加起来
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        import collections
        q = collections.deque([root])
        ans = 0
        while q:
            node = q.popleft()
            if node.left is not None:
                if node.left.left is not None:
                    ans += node.left.left.val
                if node.left.right is not None:
                    ans += node.left.right.val
                q.append(node.left)
            if node.right is not None:
                if node.right.left is not None:
                    ans += node.right.left.val
                if node.right.right is not None:
                    ans += node.right.right.val
                q.append(node.right)
        
        return ans
