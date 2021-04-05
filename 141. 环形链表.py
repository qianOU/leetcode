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
        fast = head
        while head is not None and head.next is not None:
            slow = slow.next
            fast = fast.next.next 
            if fast == slow: # 相遇作为 while 的内部退出循环条件
                break
        
        know = slow
        slow = head
        while 1:
            fast = fast.next
            slow = slow.next
            if fast == know:
                print('环状起点为：', fast.val,slow.val)
                break

        return True