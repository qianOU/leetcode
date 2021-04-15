# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 前序遍历还原树
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
       
        # 对于每一个节点构造一个上下界参数
        # 如果当前节点的值在范围之内则插入节点，否则返回，回溯到父节点进行处理
        def dfs(lower, upper):
            nonlocal index
            if index == len(preorder): # 如果遍历到最后一个元素，则结束递归
                return
            
            item = preorder[index]

            if item < lower or item > upper: # 如果不符合。则回溯给父节点进行判断
                return 
            
            # 前序遍历操作获取 preorder的元素，正好与 preorder序列来自前向遍历保持一致
            
            root = TreeNode(item)
            
            index += 1
            root.left = dfs(lower, item)
            root.right = dfs(item, upper)
            return root
        index = 0
        node = dfs(float('-inf'), float('inf'))
        return node
        
        # 基于 分治 + 二分查找
        # 因为左子树的特性是所有节点的值都是小于根节点的，
        # 右子树的特性是所有值都是大于根节点的
        # 所以我们可以找寻 前序遍历数组中，最后一个小于根结点的位置，来划分左右子树
        def fenzhi(left, right):
            if right < left:
                return
            if left == right:
                return TreeNode(preorder[left])
            
            val = preorder[left]
            root = TreeNode(val) 
            l = left + 1
            r = right
            while l <= r:
                mid = l + (r-l)//2
                if preorder[mid] > val:
                    r = mid - 1
                elif preorder[mid] < val:
                    l = mid + 1

            root.left = fenzhi(left+1, r)
            root.right = fenzhi(r+1, right)
            return root
        
        node = fenzhi(0, len(preorder)-1)
        return node