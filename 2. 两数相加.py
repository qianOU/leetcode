# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        more = 0
        pre = dum = ListNode()
        while l1 or l2 or more:
            item1 = l1.val if l1 else 0
            item2 = l2.val if l2 else 0
            cur = item1 + item2 + more
            more = cur // 10
            cur = ListNode(cur%10)
            dum.next = cur
            dum = cur
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return pre.next