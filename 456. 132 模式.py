class Solution:
    # i<j<k 要求有 num[i] < num[k] < num[j]
    # 从中可以看出 k和j 之间的关系是倒序关系，因此我们从后往前构建一个 单调递减栈，
    # 栈底保存最大值，这也就是希望找到的 j 的位置，对于 k 我们使用一个变量来保存遍历过程中，次小值，注意不能与 j 的值相等
    def find132pattern(self, nums) -> bool:
        # 单调递减栈
        stack = []
        right_max = float('-inf')
        n = len(nums)
        for i in range(n-1, -1, -1): # 倒序入栈
            item = nums[i]
            if stack and item < right_max: # 找到符合的 序列时
                return True
            while stack and stack[-1] <= item: # 单调递减栈
                right = stack.pop() # 弹出的都是 k 元素
                # 在更新 栈中 num[j] 的位置同时，也更新 理想的num[k] 的值
                if  right > right_max and right != item:
                    right_max = right
            
            stack.append(item)
        return False

print(Solution().find132pattern([-1,3,2,0]))