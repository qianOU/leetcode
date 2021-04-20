# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        
        res = []

        def dfs(root, start, end): # 左闭右开
            if  start >= end: # 如果先序遍历序列中的子序列不存在
                return root is None 
            elif root is None: # 否则。若 节点是 空 但是先序遍历显示 有子树存在
                return False
            
            head = voyage[start] 

            if root.val != head: # 如果当前节点不想等
                return False
            
            
            if root.right and root.right.val in voyage[start+1:end]: # 如果 树的右子树存在，并且也在 先序遍历的序列中
                idx =  voyage[start+1:end].index(root.right.val) + start+1 # 找到先序遍历系列中的与 root.right.val 相等的索引
                if (root.left and root.left.val == voyage[start+1]) or (root.left is None and start+1 == idx): # 两棵树左右节点值都对应时，不需要反转
                    return dfs(root.left, start+1, idx) and dfs(root.right, idx, end)
                elif idx == start+1 : # 树的右子节点，占据了 先序遍历的左子节位置时
                    if not root.left: # 如果 树不存在 左子节点，也就意味着，反转 root 节点
                        res.append(root.val)
                        return dfs(root.right, start+1, end)
                    if root.left.val in voyage[start+2:end]: # 如果树的左子节点存在， 并且处于 先序遍历中的右子节点位置时， 需要交换位置
                        mid =  voyage[start+2:end].index(root.left.val) + start+2
                        res.append(root.val)
                        return dfs(root.right, start+1, mid) and dfs(root.left, mid, end)
                else:
                    return False
            
            elif  root.right and  root.right.val  not in voyage[start+1:end]: # 若 树的右子节点存在， 但是不存在 于 先序遍历的序列中时
                return False

            elif not root.right: # 若树的右子节点不存在时， 进入下一层决策，比对树的左字节点
                return dfs(root.left, start+1, end)
        
        item = dfs(root, 0, len(voyage)) 

        if item: # 若是匹配的则，返回反转节点序列
            return res
        else:
            return [-1]

                


