# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pre = dum = ListNode(0, head)
        p = head

        def reverse(a, k): # 反转a链表的 k 个节点
            last = a
            prev = None
            count = 0
            while count < k and a: # 循环结束条件是到达了组个数，或者达到了链表末尾
                next = a.next
                a.next = prev
                prev = a
                count += 1
                a = next
            
            if count != k: # 对于最后不足 k 个的序列再反转，也就保证了原序
                pre = None
                while prev:
                   next = prev.next
                   prev.next = pre
                   pre = prev
                   prev = next
                
                return pre, None, None


            
            return prev, last, a # 返回反转后的首尾结点,以及 下一组反转链表的起始节点
        
        
        while p:
            prev, last, p = reverse(p, k)
            dum.next = prev
            dum = last
    
        
        return pre.next
