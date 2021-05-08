# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        tmp1, tmp2 = ListNode(), ListNode()
        flag = 1
        pre1, pre2 = tmp1, tmp2
        while head:
            next_ = head.next
            if flag > 0:
                tmp1.next = head
                tmp1 = tmp1.next
            else:
                tmp2.next = head
                tmp2 = tmp2.next
            
            flag *= -1
            head = next_
        
        tmp1.next = pre2.next
        tmp2.next = None
        return pre1.next