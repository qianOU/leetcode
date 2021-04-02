# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # 方法一： 将值复制到数组 + 双指针法
    def isPalindrome(self, head):
        ans = []
        while head is not None:
            ans.append(head.val)
            head = head.next
        
        left = 0
        right = len(ans)

        while left < right:
            if ans[left] != ans[right-1]:
                return False
            left += 1
            right -= 1
        return bool(ans)    

    # 方法二 快慢指针 + 逆转链表
    def isPalindrome2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 先找到中点位置
        if head is None or head.next is None:
            return True
        
        def reverse(head):
            if head is None:
                return
            prev = None
            cur = head
            while cur is not None:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            return prev

        fast = head
        slow = head
        while fast is not None:
            if fast.next is None:
                break
            fast = fast.next.next
            q = slow # 用于反转还原
            slow = slow.next
        
        # 也可以不使用 反转链表操作，使用 LIFO 的栈性质也是相当于逆序了后半部分链表的输出
        p = right = reverse(slow) 
        
        while head is not None and right is not None:
            if head.val != right.val:
                q.next = reverse(right)
                return False
            head = head.next
            right = right.next
        q.next = reverse(p)
        return True

        # 正/逆序构成数字，如果是回文串，最后数字是相等的
        def isPalindrome(self, head):
            s1 = 0
            s2 = 0
            t = 1
            while head is not None:
                s1 = s1*10 + head.val
                s2 += head.val * t
                t *= 10
            return s1 == s2

def print_link(head):
    head = head
    while head is not None:
        print(head.val)
        head = head.next

l1 = [1,2,2,1]
temp = h1 = ListNode(l1[0])
for i in l1[1:]:
    h1.next = ListNode(i)
    h1 = h1.next
l1 = temp
print_link(l1)
A = Solution()
print(A.isPalindrome(l1))
print_link(l1)

print(A.isPalindrome2(l1))