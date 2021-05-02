class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # 维护一个单调递增栈
        # 每次栈顶弹出一个元素，即可视为 移除的一个不符合要求的结果
        stack = []
        n = len(num)
        res = 0
        for i in range(n):
            while stack and num[stack[-1]] > num[i]: # 非严格单调递增栈，即遇见相等元素时不执行出栈
                if res < k:
                    stack.pop()
                    res += 1 # 没弹出一个元素时记录移除的字符次数
                else:
                    break
            
            stack.append(i)
        
       
        for j in range(k - res): # 如果原生就是大部分有序的，则删除有序的最大几位即可
            stack.pop()
        
        item = ''.join(num[i] for i  in stack).lstrip('0')
        return item if item else '0'


print(Solution().removeKdigits("1234567890", 9))