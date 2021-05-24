# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        q = [root]
        flag = 1 # -1 表示从孩子节点应该从右->左， 1 表式孩子节点应该从 左 -> 右

        ans = []
        while q:
            flag *= -1
            sz = len(q)
            row = []
            stack = []
            for _ in range(sz):
                cur = q.pop()
                row.append(cur.val)
                tmp = [cur.left, cur.right]
                if flag > 0: # 正序输出 从 左-> 右， 也就意味着 倒序入栈
                    stack.extend(i for i in tmp[::-1] if i)
                else:
                    stack.extend(i for i in tmp if i)
            
            q = stack
            ans.append(row)
        
        return ans

