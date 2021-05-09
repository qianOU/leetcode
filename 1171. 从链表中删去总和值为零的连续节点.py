# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 实际上，只要使用hash表记录前缀和相同的最右边元素，那么两者之间的元素之和为0，是可以被删除的
# 所以引出方法2
class Solution:
    # 单纯使用栈的思想， 前缀和 + 栈以及辅助栈
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        from collections import defaultdict
        records = [0]
        stack = []
        pre = dummy = ListNode(None)
        
        cumsum = 0
        while head:
            val = head.val
            cumsum = records[-1] + val
            head = head.next
            if cumsum in records:
                    while records:
                        if records[-1] == cumsum:
                            break
                        stack.pop()
                        records.pop()
                        
                    continue
                    
            records.append(cumsum)
            stack.append(val)
            

        for i in stack:
            item = ListNode(i)
            dummy.next = item
            dummy = dummy.next
        
        return pre.next
        

    
    # 方法二 ： 使用hash表 记录等于这个前缀和的最右边的节点
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        from collections import defaultdict
        records = defaultdict(ListNode)
        dum = ListNode(0, head)
        p = dum
        pre_sum = 0
        while p:
            val = p.val
            pre_sum += val
            records[pre_sum] = p #  使用hash表 记录等于这个前缀和的最右边的节点
            p = p.next
        
        p = dum
        cur_sum = 0
        while p: 
            cur_sum += p.val
            p.next = records[cur_sum].next # 删除前缀和相等的中间部分,如果没有该前缀和对应那就是自身下一个节点
            p = p.next 
        
        return dum.next

