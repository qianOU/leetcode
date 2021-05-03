# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = dummy = ListNode() # 虚拟节点
        p = head
        while p and p.next:
            next_p = p.next.next # 记录下一次交换的起始位置
            pre.next =  p.next # step 1
            pre.next.next = p # step 2 进行交换 1，2
            p = next_p # 执行下一层交换
            pre = pre.next.next # 更新新链表的指针位置
    
        pre.next = p # 如果链表是奇数节点时
    
        return dummy.next 