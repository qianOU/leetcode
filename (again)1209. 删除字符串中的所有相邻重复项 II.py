class Solution:
    # 方法 1：使用栈
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] #栈中元素记载了 当前元素，以及 重复的次数
        for  i in s:
            if stack and i == stack[-1][0]:
                count = stack[-1][-1]
                stack.append((i, count + 1))
                if count+1 >= k:
                    for _ in range(k):
                        stack.pop()

            else:
                stack.append((i, 1))  
    
            
        return ''.join(i[0] for i in stack)
    
    # # 双指针之 ——快慢指针
    # def removeDuplicates(self, s: str, k: int) -> str:
    #     pass
        # slow = fast = 0
        # n = len(s)
        # while fast < n:
        #     while fast < n and s[slow] == s[fast]:
        #         fast += 1
            
        #     if fast - slow + 1 >= k:
        #             slow =

print(Solution().removeDuplicates("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", 4))