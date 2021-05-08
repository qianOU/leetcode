# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        pre = head
        for i in range(k-1):
            pre = pre.next
        
        fast = pre
        slow = head
        while fast.next: # fast.next 表示在链表末尾节点终止
            fast = fast.next
            slow = slow.next
        
        slow.val, pre.val = pre.val, slow.val

        return head