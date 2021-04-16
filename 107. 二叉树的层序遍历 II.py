# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
 
        import collections
        # 方法1 层次遍历 加 反转列表
        def bfs(root):
            if not root:
                return []
            
            q= collections.deque([root])
            results = []
            while q:
                sz = len(q)
                ans = []
                for i in range(sz):
                    top  = q.popleft()
                    ans.append(top.val)
                    if top.left:
                        q.append(top.left)
                    if top.right:
                        q.append(top.right)
                results.append(ans)
            
            n = len(results)
            # 倒序列表 results
            for i in range(len(results)//2):
                results[i], results[n-1-i] = results[n-1-i], results[i]
            
            return results

        return bfs(root)

  