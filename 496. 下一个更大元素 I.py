class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # 单调栈
        stack = []
        ans = dict.fromkeys(nums2)
        n = len(nums2)
        for i in range(n-1, -1, -1): # 倒序入栈 
            while stack and stack[-1] <= nums2[i]: #确保栈是单调递减的
                stack.pop()
            
            ans[nums2[i]] = -1 if not stack else stack[-1]
            stack.append(nums2[i])
        # return ans
        # print(ans)

        
        return [ans[i] for i in nums1]

print(Solution().nextGreaterElement([4,1,2],[1,3,4,2]))


