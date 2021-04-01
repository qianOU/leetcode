# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList_iter(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return 
        
        prev = None
        cur = head
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        return prev


    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def bt(head):
            if head is None:
                return 
            if head.next is None:
                return head
        
            next = bt(head.next)
            head.next.next = head
            head.next = None
            return next
        