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
    # 使用递归的归并排序
    def sortList(self, head: ListNode) -> ListNode:
        def merge(a, b):
            prev = dummy = ListNode(float('-inf'))
            while b and a:
                
                if b.val < a.val:
                    prev.next = b
                    b = b.next      
                else:
                    prev.next = a
                    a = a.next
                
                prev = prev.next     
                
            if b:
                prev.next = b # 将dumy尾部和 b 接上
            else:
                prev.next = a
            return dummy.next

        # 左闭右开区间 
        def getmid(left, right):
            slow = fast = left
            while fast is not right and fast.next is not right: #终结条件是否接触到右边节点
                fast = fast.next.next
                slow = slow.next
            
            return slow
        
        def sort(left, right): # 左闭右开区间
            if left is right:
                return None
            if left.next is right: # 如果只有一个元素的时候，需要返回该元素节点，并且需要将node指向None
                left.next = None #### 十分注意
                return left
            mid = getmid(left, right)
            tmp1 = sort(left, mid)
            tmp2 = sort(mid, right)
            return merge(tmp1, tmp2)
        
        return sort(head, None)

# 使用自底向上的归并排序
class Solution:
    # 使用迭代的归并排序（自底向上）
    def sortList(self, head: ListNode) -> ListNode:
        def merge(a, b):
            prev = dummy = ListNode(float('-inf'))
            while b and a:
                
                if b.val < a.val:
                    prev.next = b
                    b = b.next      
                else:
                    prev.next = a
                    a = a.next
                
                prev = prev.next     
                
            if b:
                prev.next = b # 将dumy尾部和 b 接上
            else:
                prev.next = a
            return dummy.next

        if not head:
            return 
        
        dum = ListNode(0, head)

        length = 0
        p = dum
        while p:
            p = p.next
            length += 1

        sub = 1
        while sub < length:
            pre, cur = dum, dum.next
            while cur: # head1 head2 原则上是等长的
                head1 = cur
                for i in range(1, sub):
                    if cur and cur.next:
                        cur = cur.next
                    else: # 不能凑成完整的一组时
                        break
                
                head2 = cur.next
                cur.next = None
                cur = head2
                for i in range(1, sub):
                    if cur and cur.next:
                        cur = cur.next
                    else:
                        break
                suc = None
                if cur:
                    suc = cur.next
                    cur.next = None
                new = merge(head1, head2)
                pre.next = new

                while pre.next: # 找到合并组后的最后一个节点,作为下一组合并节点的头节点
                    pre = pre.next
                
                cur = suc
            
            sub <<= 1
        return dum.next

dum = pre = ListNode()
for i in [4,2,1,3]:
    tmp = ListNode(i)
    dum.next = tmp
    dum = dum.next

def print_(a):
    while a:
        print(a)
        a  = a.next
# print_(pre.next)
print_(Solution().sortList(pre.next))