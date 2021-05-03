"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        arr = []
        head2 = head
        records = {None:None} # 记录 原链表节点和位置的索引关系
        rands = {None:None} # 记录 原链表 随机节点和索引的对应关系
        records2 = {None:None} # 记录 索引和新建链表节点的关系
        idx = 0
        while head:
            records[head] = idx
            head = head.next
            idx += 1
        
     
        dummy3 = dummy2 = dummy = ListNode()
        idx = 0
        while head2:
            item = ListNode(head2.val)
            records2[idx] = item
            rands[item] = records[head2.random]
            dummy.next = item # 构建新链表
            dummy = dummy.next
            head2 = head2.next
            idx += 1


        dummy2 = dummy2.next
        while dummy2:
            dummy2.random = records2.get(rands[dummy2]) # 添加上节点映射关系
            dummy2 = dummy2.next

        return dummy3.next   

