# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 使用快速排序
    def sortList(self, head: ListNode) -> ListNode:
        arr = []
        head2 = head
        
        while head:
            arr.append(head.val)
            head = head.next
        
        import random
        random.shuffle(arr)

        def quick(start, end): # 左闭右开区间
            # print(arr[start:end], start, end)
            if end <= start:
                return 

            k = arr[start] # base 元素
            
            # 左闭右闭进行搜索区间
            left = start + 1
            right = end - 1
            
            while left <= right: # 使用左闭右闭的判定条件
                while  left < end and arr[left] <= k:
                    left += 1

                while right >=0 and arr[right] > k:
                    right -= 1

                if left >= right: # 只有left 小于 right 时，才需要交换left， right 的位置
                    break
                
                arr[left], arr[right] = arr[right], arr[left]

            # 确保了 [right, end） 是 大于 k 的
            #[left, right) 是小于 k 的
            # 交换头位置（基准位置）与 right 的值， 
            arr[start], arr[right] = arr[right], arr[start]

            quick(start, right) 
            quick(left, end)

        quick(0, len(arr))
        pre = dummy = ListNode()
        for i in arr:
            dummy.next = ListNode(i)
            dummy = dummy.next
        
        return pre.next
            


class Solution:
    # 使用归并排序
    def sortList(self, head: ListNode) -> ListNode:
        



