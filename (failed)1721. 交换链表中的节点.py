# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        count = 0
        dummy = ListNode()
        dummy.next = head
        head = dummy
        ans = [[] for i in range(k)]
        prev = pre_1 = after_1 = None

        while head: 
            print(head.val,count, k)
            if count == k:
                
                prev_1 = prev
                after_1 = head.next
            ans[(count-1)%k]=[prev, head.next]
            prev = head 
            head = head.next
            count += 1

        print(ans)
        prev_2, after_2 = ans[(count-1)%k]
        print(ans[(count-1)%k])
        tmp = prev_1.next
        if tmp is prev_2:
            prev_1.next = prev_2.next
            prev_1.next.next = prev_2
            prev_2.next = after_2
            return dummy.next
        prev_1.next = prev_2.next
        prev_1.next.next = after_1
        prev_2.next = tmp
        prev_2.next.next = after_2
        return dummy.next
    
head = pre = ListNode()
for i in [7,9]:
    tmp = ListNode(i)
    head.next = tmp
    head = head.next

print(Solution().swapNodes(pre.next, 2))