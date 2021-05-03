# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 找寻链表中点
        prev = fast = slow = head
        count = 0
        while fast and fast.next:
            count += 1
            prev = slow
            fast = fast.next.next
            slow = slow.next
        prev.next = None
        
        if count == 0: # 如果链表只有一个元素时，无需处理
            return 
        # 反转后半部分
        prev = None
        cur = slow
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        start = p =  head
        # 当链表节点个数大于1个时， 注意此处只有可能是 p 指向的链表 等于或者优于 prev 指向的链表先消耗完
        while p and prev:
            tmp = p.next
            head.next = prev
            prev = prev.next
            head.next.next = tmp
            last = head.next # 用于处理当 p 节点遍历到末尾时， prev 依然还有节点未遍历
            head  = last.next
            p = tmp
            

        if prev:
            last.next = prev # 将prev 未遍历的元素添加进来
       
