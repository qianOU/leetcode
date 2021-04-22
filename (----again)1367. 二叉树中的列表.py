# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:

        if head is None:
            return True
        if root is None:
            return False

        # 定义check 检查head链路 是否 在root为序列起点的子树上 
        # 以 root 为 起点
        def check(root, head):
            if head is None:
                return True
            if root is None:
                return False
            if root.val != head.val:
                return False
            
            return check(root.left, head.next) or check(root.right, head.next)
        
        # 检查当前节点是否是满足题意的子树上的起始序列，
        # 查看左子树是否满足题意
        # 查看右子树是否满足提议 
        return check(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)