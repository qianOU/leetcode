import bisect
class Solution:
    # 栈
    def decodeAtIndex(self, s: str, k: int) -> str:
        n = len(s)
        cur = 0
        count = 0
        precount = [0]
        stack = []
        while cur < n and count < k:
            tmp = ''
            while cur < n and s[cur].isalpha():
                tmp += s[cur]
                cur += 1
                count += 1
     
            if cur < n and s[cur].isdigit():
                repeat = int(s[cur])
                count *= repeat
                stack.append(tmp)
                precount.append(count)
                if count >= k: 
                    break
                cur += 1

        if cur == n and s[-1].isalpha(): #  特殊情况
            stack.append(tmp)
            precount.append(count)

        print(stack, precount)

        def dfs(cur, total):
            m = len(stack[cur])
            leng = m + precount[cur]
            res = total % leng
            if res == 0: 
                while not stack[cur]:
                    cur -= 1
                return stack[cur][-1]
            elif res > precount[cur]:
                return stack[cur][res - precount[cur] - 1]

            idx = bisect.bisect_left(precount, res)
            return dfs(idx - 1, res)

        return dfs(len(stack)-1, k)


# 官方思路
class Solution:
    # 官方逆向考虑：一次遍历
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for i in range(len(s)):
            if s[i].isalpha():
                size += 1
            else:
                size *= int(s[i])

            if size >= k: break # 剪枝
        
        # 反向还原
        for j in s[i:None:-1]:
            k %= size
            if k == 0 and j.isalpha(): 
                return j
            elif j.isdigit():
                size //= int(j)
            else:
                size -= 1