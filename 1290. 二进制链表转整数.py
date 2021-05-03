# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            bit = int(head.val)
            ans <<= 1 
            ans += bit
            head = head.next
        
        return ans