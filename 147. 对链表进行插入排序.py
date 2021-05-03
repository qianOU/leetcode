# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur =  dummy = ListNode(float('-inf'))
        while head:
            item = head.val
            next_one = head.next

            cur = dummy
            while cur:
                # 在中部插入
                if cur.val > item:
                    prev.next = head
                    head.next = cur
                    break
                prev = cur
                cur = cur.next
                
            
            # 如果需要在末尾插入
            if not cur:
                head.next = None # 切记此处需要将，最后链表节点指向None
                cur.next = head
            
            head = next_one
        
        return dummy.next