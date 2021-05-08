# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return str(self.val)

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
        def merge(a, b):
            pre = dummy = ListNode(float('-inf'))
            dummy.next = a

            #找到尾部节点
            # while a.next:
            #     a = a.next
            # dummy_last = a
            prev = dummy
            while b and dummy:
                # print(b, dummy)
                if b.val < dummy.val:
                    next = b.next
                    prev.next = b
                    b.next = dummy
                    dummy = b
                    b = next
                    
                    
                    

                prev = dummy
                dummy = dummy.next
                
                
                
            if b:
                prev.next = b # 将dumy尾部和 b 接上

            return pre.next

        # 左闭右开区间
        def getmid(left, right):
            slow = fast = left
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            
            return slow
        
        def sort(left, right):
            print(left, right)
            if left is right:
                return None
            if left.next is right:
                return left
            mid = getmid(left, right)
            b = mid.next
            mid.next = None
            tmp1 = sort(left, mid)
            tmp2 = sort(mid, right)
            return merge(tmp1, tmp2)
        
        return sort(head, None)


dum = pre = ListNode()
for i in [4,2,1,3]:
    tmp = ListNode(i)
    dum.next = tmp
    dum = dum.next

def print_(a):
    while a:
        print(a)
        a  = a.next

print_(Solution().sortList(pre.next))