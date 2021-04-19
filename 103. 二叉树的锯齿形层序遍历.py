# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        def bfs(root):
            if root is None:
                return []
            q = [root] # 当前遍历节点栈
            flag = 1 #控制奇偶数层
            results = []
            # 由于发现每一次遍历到当前节点时，其孩子节点具有后入先出的特性，
            # 并且需要考虑 在 不同层级 孩子节点入栈的顺序是不同的
            # 维护两个栈
            while q:
                sz = len(q)
                ans = []
                stack = [] # 存储孩子节点的栈
                for _ in range(sz):
                    node = q.pop()
                    ans.append(node.val)
                    temp = [ node.right, node.left]
                    if flag < 0: #当前在偶数层，下一层需要先遍历左子节点，因此左子节点后序入栈
                        stack.extend(i for i in temp if i)
                    if flag > 0: #当前在奇数层，下一层需要先遍历右子节点，因此右子节点后序入栈
                        stack.extend(i for i in temp[::-1] if  i)
                flag *= -1
                results.append(ans)
                q = stack # 进入下一层决策
            return results
        
        return bfs(root)