# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # list2 的尾端节点
        end_2 = list2
        while end_2.next:
            end_2 = end_2.next
        
        left_node = right_node = list1

        count = 0
        while right_node:
            if count == a-1:
                left_node = right_node
            elif count == b+1:
                break

            right_node = right_node.next
            count += 1
        
        left_node.next =  list2
        end_2.next = right_node
        return  list1


s