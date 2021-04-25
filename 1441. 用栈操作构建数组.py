class Solution:
    # 使用数组完成
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        num = list(range(1, n+1))
        j = 0
        len_t = len(target)
        for i in num:
            if i == target[j]:
                res.append('Push')
                j += 1
            if i < target[j]:
                res.append('Push')
                res.append('Pop')
            if i > target[j] or j == len_t:
                return res
    
    # 使用栈
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack1 = []
        stack2 = [] # 用来保存符合要求的匹配项
        for i in range(1, n+1):
            if i == target[len(stack2)]: # 和栈顶元素进行比较
                stack1.append('Push')
                stack1.append(i)
            elif i < target[len(stack2)]:
                stack1.append('Push')
                stack1.append('Pop')
            if len(stack2) == len(target):
                return stack1