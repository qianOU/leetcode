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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 二叉搜索树的中序遍历是有序的
        
        def dfs():
            nonlocal head
            if head is None:
                return None
            
            item = head.val
            head = head.next

            left = dfs()
            root = TreeNode(item)
            right = dfs()

            root.left = left
            root.right = right
            return root
        
        return dfs()