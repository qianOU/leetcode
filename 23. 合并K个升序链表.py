# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 方法一，两两合并
        def merge(a, b):
            pre = dum = ListNode()
            while a and b:
                if a.val < b.val:
                    pre.next = a
                    a = a.next
                else:
                    pre.next = b
                    b = b.next
                
                pre = pre.next
            
            if a:
                pre.next = a
            else:
                pre.next = b
            
            return dum.next
        
        from functools import reduce
        return reduce(merge, lists, ListNode(float('-inf'))).next
    
    # 方法二，使用优先队列，即堆保证有序
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        from queue import PriorityQueue
        p = PriorityQueue()
        import heapq
        p = []
        count = 1
        for i in lists:
            # p.put((i.val, i))
            if i:
                heapq.heappush(head, (i.val, i))
        pre = dum = ListNode()
        while p:
            count += 1
            item = p.get()
            if item.next:
                heapq.heappush(head, (item.next.val, item.next))
            dum.next = item
            dum = dum.next
        dum.next = None
        return pre.next