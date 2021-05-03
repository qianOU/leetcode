class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast:
            while fast and fast.val == slow.val:
                fast = fast.next
            
            slow.next = fast
            slow = slow.next
        
        return head