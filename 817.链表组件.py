# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        nums = set(G)
        count = 0
        connect = 0 # 计数一个组件里面的元素个数

        while head:
            item = head.val
            head = head.next
            
            if item  in nums:
                connect += 1
            else:
                connect = 0

            if connect == 1: #为了确保每次组件只计算一次，故只对计数为 1 状态的组件进行计数
                    count += 1
        
        return count
