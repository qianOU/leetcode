class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # 单调栈 找寻下一个小的元素
        stack = []
        total = 0
        n = len(arr)
        res = [n] * n
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            stack.append(i)
           
