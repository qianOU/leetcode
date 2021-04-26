class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        ans = list(s)

        while True:
            stack = []
            is_repeat = 0
            count = 0
            for  i in ans:
                if stack and i == stack[-1]:
                    stack.append(i)
                    count += 1
                    if count >= k:
                        is_repeat = 1 # 表示是否触发了删除
                        for _ in range(k):
                            stack.pop()
                        count = 0 # 恢复到默认值

                else:
                    stack.append(i)  
                    count = 1
            
            ans = stack
            # print(ans)
            if not is_repeat:
                return ''.join(ans)

print(Solution().removeDuplicates("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", 4))