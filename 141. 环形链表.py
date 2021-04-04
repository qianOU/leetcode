# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        
        slow = head
        fast = head.next.next
        while slow != fast:
            slow = slow.next
            if fast is None or fast.next is None:
                return False
            else:
                fast = fast.next.next 
        know = slow
        slow = head
        while fast != know:
            fast = fast.next
            slow = slow.next

        return True

            
