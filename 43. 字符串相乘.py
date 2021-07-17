class Solution:
    # 思路1： 朴素的竖式乘法 即 乘数的每一位 与 被乘数 相乘，记得添 0 ，最后做字符串加法
    def multiply(self, num1: str, num2: str) -> str:

        def dfs(num1, num2):
            if not num2:
                return ''
            
            # 将 num2[-1] 和 num1 的乘积存入 res 变量中
            res = ''
            cur = int(num2[-1])
            more = 0
            for i in num1[::-1]:
               more, now = divmod(int(i) * cur + more, 10)
               res += str(now)
            
            # 查看最后是否需要进位
            if more:
                res += str(more)
            
            res = res[::-1]
 

            # 得到 num2[-2] 和 num1 的每 一位 乘积，别忘了 乘以 10 即 加 ‘0’
            other = dfs(num1, num2[:-1]) + '0'


            # 将res 和 other 做加法 数字合并
            ans = ''
            st1, st2 = len(res) - 1, len(other) - 1
            more = 0
            while st1 >= 0 or st2 >= 0 or more:
                item1 = int(res[st1]) if st1 >= 0 else 0
                item2 = int(other[st2]) if st2 >= 0 else 0
                more, cur = divmod( item1 + item2 + more, 10)
                ans += str(cur)
                st1, st2 = st1 - 1, st2 - 1


            item = ans[::-1].lstrip('0')
    
            
            return item if item else '0'
        
        return dfs(num1, num2)

    # 思路2： 优化的竖式乘法 即 乘数的每一位 与 被乘数的每一位 相乘
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        # 倒序遍历是必须的，为了 正确处理 进位的情况
        for i in range(m-1, -1, -1):
            one = int(num1[i])
            for j in range(n-1, -1, -1):
                two = int(num2[j])
                sum1 = res[i+j+1] + one*two
                res[i+j+1] = sum1 % 10
                res[i + j] += sum1 // 10 # 不需要考虑进位是因为 i+j是递减变化的,下一次会 进行 求余， 并进行进位
        
        ans = ''
        for i in res:
            if i or ans: ans += str(i)
        return ans if ans else '0'


print(Solution().multiply(
"123",
"456"
))