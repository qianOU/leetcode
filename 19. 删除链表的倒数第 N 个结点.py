# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dum = ListNode(0, head)
        length = 0
        p = dum.next
        while p:
            length += 1
            p = p.next

        fast = dum
        for i in range(length - n): # 倒数第n个，也就是 正数 length - k 个
            fast = fast.next

        tmp = fast.next.next
        fast.next = tmp
        return dum.next
        