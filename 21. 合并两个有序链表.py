# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)



class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def backtrace(l1, l2):
            # base case
            if l1 is None and l2 is None:
                return None
            elif l1 is not None and l2 is None:
                return l1
            elif l2 is not None and l1 is None:
                return l2

           
        
            # 确保：l1 是最小节点
            if l1.val > l2.val:
                l1, l2 = l2, l1
            
            res = backtrace(l1.next, l2)

            l1.next = res
            return l1
        
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        head = backtrace(l1, l2)
        return head


def print_link(head):
    while head is not None:
        print(head.val)
        head = head.next


l1 = [5]
l2 = [1,2,4]
temp = h1 = ListNode(l1[0])
for i in l1[1:]:
    h1.next = ListNode(i)
    h1 = h1.next
l1 = temp

temp = h2 = ListNode(l2[0])
for i in l2[1:]:
    h2.next = ListNode(i)
    h2 = h2.next
l2 = temp

# print_link(l1)
print_link(l2)

a = Solution().mergeTwoLists(l1, l2)
print_link(a)