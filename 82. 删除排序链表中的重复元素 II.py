# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return 
        slow, fast = head, head.next
        pre = ans = ListNode()

        while fast:
            while fast and fast.val == slow.val:
                fast = fast.next
            
            if not fast:
                break

            if slow.next is fast: # slow 对应的节点没有重复值时，
                ans.next = slow
                ans = ans.next
                

            slow = fast
            fast = fast.next
        
        ans.next =  slow if not slow.next else None # 处理 slow 是末尾节点的情况
        return pre.next