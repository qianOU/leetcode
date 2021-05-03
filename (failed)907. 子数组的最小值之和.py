
           
class Solution:
    def sumSubarrayMins(self, arr) -> int:
        # 非严格单调递增栈
        stack = []
        n = len(arr)
        ans = 0
        for idx in range(n):
            count = 0
            while stack and arr[stack[-1]] > arr[idx]:
                top = stack.pop()
                count += 1
                ans += arr[top] * count

            # if not stack:
            #     ans += 

            stack.append(idx)
        
        print(ans, stack)
        # 对单调递增栈内元素做最后计算
        m = len(stack)
        for i in range(m):
            item = stack.pop()
            ans += arr[item] * (i + 1)
        
        return ans +  m * arr[item]

print(Solution().sumSubarrayMins([11,81,94,43,3]))