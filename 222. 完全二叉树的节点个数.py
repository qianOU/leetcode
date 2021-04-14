# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left  = root
        depth = -1 # 树的深度
        while left is not None:
            depth += 1
            left = left.left

        if depth == 0:
            return 1

        # 查看 num 的二进制表示是否在树中
        def isvalid(num, level):
            tmp = root
            pair = 1<< (level-1)
  
            while tmp is not None and pair > 0:
                # print('-', bin(pair), pair & num, num, pair)
                # num 二进制的 次最高位 一直到最低位 表示 从根节点的变化过程
                if (pair & num):
                    tmp = tmp.right
                else:
                    tmp = tmp.left
                pair = pair >> 1
             
            if  pair==0 and tmp is not None:
                return True
            else:
                return False

        # 得到 树节点数目的取值范围为 [2^h, 2^(h+1) - 1]
        left = 1 << depth
        right = (1<<(depth+1)) - 1
        while  left <= right:
            mid = left + (right-left) // 2
            if isvalid(mid, depth): # 表示 mid 在树中，需要收缩左边界
                left = mid + 1
            else:
                right = mid - 1
        
        return left - 1