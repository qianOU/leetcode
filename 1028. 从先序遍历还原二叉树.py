# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        import re
        def dfs(d):
                nonlocal s
                if not s:
                    return 
                # 方法一： 使用指针处理, 主要模拟了正则的功能
                depth = 0
                left = 0
                item = ''
                if s[0] != '-': # 字符串的首个元素
                    while left < len(s):
                        if s[left] == '-':
                            break
                        item += s[left]
                        left += 1
                else:
                    while left < len(s):
                        if s[left] == '-' and flag:
                            if 0 < depth <= d:
                                return
                            break
                        if s[left] == '-':
                            depth += 1
                        else:
                            flag = 1
                            item += s[left]
                
                s = s[left:]
                item = int(item)
                #  方法二： 使用 正则 方式
                # item, depth = re.search('(\d+)(-*)', s).groups()
                # depth = len(depth)

                # if 0< depth  <=d: #当下一个节点的深度，小于等于当前节点深度时，要回溯给父亲节点处理
                #     return 
                
                # s = s[len(items)+depth:]

                node = TreeNode(int(item))

                node.left = dfs(depth)
                node.right = dfs(depth)

                return node

                
        return dfs(S, 0)