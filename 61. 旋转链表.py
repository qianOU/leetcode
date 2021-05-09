# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 更加具体的思路，可以是将某位节点与头节点链接，形成闭环，再在 length - k 处断开即可
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return 
        
        if not k:
            return head

        dum = ListNode(0, head)
        length = 0
        p = head
        while p:
            length += 1
            prev = p # 用来记录链表最后的节点.主要用来处理旋转的时候的连接性
            p = p.next
        
        k = k % length
        
        if k == 0: # 不需要进行旋转时
            return head
        
        fast = dum
        for i in range(length - k): # 需要旋转k步，也就是在 length-k处断开
            fast = fast.next
        

        two = fast.next # 后半部分
        fast.next = None # 断开连接
        
        prev.next = head # 将后半部分与头部链接
        return two
        
