# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 环形链表处理的过程包括两步骤：
    # 1.  使用快慢指针（1步，2步间隔）找到相交点
    # 2. 从相交节点 以及 头节点同时出发，遇见的第一个节点就是环的起始点
    def detectCycle(self, head: ListNode) -> ListNode:
        p1 = p2 = head
        flag = 0
        while p1 and p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 is p2:
                flag = 1
                break
            
        
        if not flag:
            return
        
        while p1 and head:
            if p1 is head:
                return head

            p1 = p1.next
            head = head.next

           
            