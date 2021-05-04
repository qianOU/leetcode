# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 反转链表
        def reverse(head):
            pre = None
            while head:
                next = head.next
                head.next = pre
                pre = head
                head = next
            
            return pre

        l1 = reverse(l1)
        l2 = reverse(l2)

        pre = dummy = ListNode()
        more  = 0
        while l1 and l2:
            item1 = l1.val
            item2 = l2.val       
            node = ListNode((more + item1 + item2) % 10)  
            dummy.next = node
            dummy = dummy.next   
            if item1 + item2 + more >= 10:
                more = 1
            else:
                more = 0
            
            l1 = l1.next
            l2 = l2.next
        
        # 如果需要进位的情况
        while l1:
            item = l1.val
            node = ListNode((more + item ) % 10) 
            if item + more >= 10:
                more = 1
            else:
                more = 0
            dummy.next = node
            dummy = dummy.next
            l1 = l1.next
        

        while l2:
            item = l2.val
            node = ListNode((more + item ) % 10) 
            if item + more >= 10:
                more = 1
            else:
                more = 0
            dummy.next = node
            dummy = dummy.next
            l2 = l2.next
        
        # # 如果最高位需要进位的情况
        if more:
            dummy.next = ListNode(1)

        # 三次反转链表
        return reverse(pre.next)
    

    # 方法二：由于逆序处理，可以考虑使用栈
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = [], []
        while l1:
            p.append(l1.val)
            l1 = l1.next
        
        while l2:
            q.append(l2.val)
            l2 = l2.next
    
        carry = 0 # 用以标记进位处理的标志
        ans = None # 用于标记新链表的头节点
        while p or q or carry: # 巧妙呀！！！
            a = 0 if not p else p.pop()
            b = 0 if not q else q.pop()
            item = a + b + carry
            node = ListNode(item % 10)
            carry = item // 10
            node.next = ans
            ans = node
        
        return ans