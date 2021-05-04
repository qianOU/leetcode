# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        length = 0
        l = root
        while l:
            length += 1
            l = l.next
        
        part = length // k
        more = length % k
        
        count = 1
        ans = []
        total = 0 # 记录当前处理的是第几个部分，主要是应对前几个部分的长度是要求大于等于后部分长度的
        while root:
            if  count == 1:
                ans.append(root)
                total += 1
                this_length = part + 1 if total <= more else part

            if count == this_length:
                next = root.next
                root.next = None # 到分割位置时，将末尾指针指向 None
                root = next
                count = 1
                continue

            root = root.next
            count += 1

        if len(ans) < k: # 如果不足，则补None
            ans.extend([None] * (k-len(ans)))

        return ans 
            