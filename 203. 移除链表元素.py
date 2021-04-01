# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head  is None:
            return None
        
        prev = head
        p1 = head.next
        while p1 is not None:
            
            if p1.val == val:
                p1 = p1.next
                continue
            prev.next = p1
            prev = prev.next
            p1 = p1.next

        prev.next = None

        if head.val == val:
                head = head.next

        return head

head = [1,2,6,3,4,5,6]
p2 = p1 = ListNode(head[0])
for i in range(1, len(head)):
    s = ListNode(head[i])
    p1.next = s
    p1 = p1.next

A = Solution()
q =A.removeElements(p2, 6)
while q is not  None:
    print(q.val)
    q = q.next
# print(A.removeElements(p2, 6).val)
