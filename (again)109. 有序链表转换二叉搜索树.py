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
    # 使用数组存放元素，主要目的还是为了获取中点位置，作为根节点，可以确保树生成的平衡性
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        # 事先遍历链表，存入数组之中
        a = list()
        while head:
            a.append(head.val)
            head = head.next
        
        n = len(a)
        # 左闭右闭区间
        def dfs(left, right):
            # 去除不合理的界限情况，防止索引越界错误
            if left > right or left < 0 or right >= n:
                return
            tmp = (left + right + 1) // 2
            root = TreeNode(a[tmp])
            root.left = dfs(left, tmp -1)
            root.right = dfs(tmp+1, right)
            return root
        
        return dfs(0, len(a)-1)
        
    # 基于快慢指针获取中点位置
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def get_mid(left, right):
            fast = slow = left
            while fast is not right and fast.next is not right: # 确保fast能走两步不越界
                fast = fast.next.next 
                slow = slow.next
            
            return slow
        
        # 左闭右开的链路区间
        def build(left, right):
            if left is right:
                return 
            
            mid = get_mid(left, right)
            root = TreeNode(mid.val)
            root.left = build(left, mid)
            root.right = build(mid.next, right)
            return root
        
        return build(head, None)