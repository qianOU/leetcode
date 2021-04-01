# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 一般无环链表相交的问题都需要 先找寻 长度差，让长链表多走 长度差步。之后齐头找寻相加点
#  对于找寻链表环的起点的情况，使用 快慢指针找到相遇节点，之后使其中任意一个指针重新指向头节点，再两指针同时前进，第一次相遇就说环的起始位置
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        count_A, count_B = 0, 0
        # 1.让二者分别走到链表末尾，测出各自长度
        while p1 is not None:
            count_A += 1
            p1 = p1.next
        while p2 is not None:
            count_B += 1
            p2 = p2.next
        
        p1 = headA
        p2 = headB
        diff = count_A - count_B
        #  2.得到分别链长的差值，让长的先走这个差值
        if diff > 0:
            while diff:
                p1 = p1.next
                diff -= 1

        elif diff < 0:
            while diff:
                p2 = p2.next
                diff += 1
        
        # 3.两指针往前走，相遇即为所求, 剩下的路径一定是一样长的
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1
