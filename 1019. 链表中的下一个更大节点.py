# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 单调栈
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        l_head = head
        n = 0 # 长度
        # 倒序链表
        prev = None
        while l_head:
            next = l_head.next
            l_head.next = prev
            prev = l_head
            l_head = next
            n += 1
        
        ans= [0] * n
        stack = []
        
        # cur 记录当前 位于原始链表的索引
        cur = n
        while prev: # 倒序遍历链表
            cur -= 1
            while stack and stack[-1] <= prev.val:
                stack.pop()
            if stack:
                ans[cur] = stack[-1]
            stack.append(prev.val)

            prev = prev.next # 链表下一个节点
        
        return ans
        