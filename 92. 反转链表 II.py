# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
        pre = dummy  = ListNode() # 虚拟节点用于处理头节点元素的情况
        dummy.next = head
        interval = right - left + 1
        count = 0
        head = dummy
        while head:
            if count == left-1:
                pre_left = head
            elif count == right:
                right = head
            
            head = head.next
            count += 1

        left = pre_left.next
        # 右半部分
        right_last = right.next
        
        # 反转中间部分
        prev = None
        cur = left
        
        while interval > 0:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            interval -= 1

        left.next = right_last
        pre_left.next = prev

        return pre.next