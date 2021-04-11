# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 回溯算法
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []

        res = []
        def backtrace(root, record):
            if root.left is None and root.right is None:
                res.append(record.copy())
                return 
            
            
            # 下一层选择 其一 走左子树
            if root.left is not None:
                #  做选择
                record.append(str(root.left.val))
                backtrace(root.left, record)
                # 撤回选择
                record.pop()

            # 下一层选择 其二 走右子树
            if root.right is not None:
                record.append(str(root.right.val))
                backtrace(root.right, record)
                # 撤回选择
                record.pop()

        backtrace(root, [str(root.val)])
        return ['->'.join(i) for i in res]

        # bfs
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        
        q = [root]
        records = [str(root.val)]
        ans = [] # 最后答案数组
        while q:
            sz = len(q)
            for _ in range(sz):
                node = q.pop(0)
                item = records.pop(0)
                #print(node.val, item)
                if node.left is None and node.right is None: # 遇见叶子节点时
                    ans.append(item)
                    continue

                if  node.left is not None:
                    q.append(node.left)
                    records.append(item+'->'+str(node.left.val))

                if  node.right is not None:
                    q.append(node.right)
                    records.append(item+'->'+str(node.right.val))
        
        return ans

    # dfs  前序遍历
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        def dfs(root, path=''):
            if root:
                # 根节点操作
                path += str(root.val)
                if root.left is None and root.right is None: #叶子节点
                    paths.append(path)
                
                else:
                    path += '->'
                    dfs(root.left, path)
                    dfs(root.right, path)
            
        paths = []
        dfs(root, '')
        return paths
