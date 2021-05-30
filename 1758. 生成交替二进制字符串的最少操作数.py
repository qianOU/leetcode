class Solution:
    # 错误!!!! 基于最长交替二进制字符串的贪心规则是错误的
    def minOperations(self, s: str) -> int:
        s = s+ s[-1]
        n = len(s)
        max_len  = 0
        ans = []
        stack = []
        for i in range(n):
            if not stack:
                stack.append(i)
                continue
            elif s[stack[-1]] == s[i]:
                q = len(stack)
                if max_len < q:
                    ans = [stack[0]]
                    max_len = q
                elif max_len == q:
                    ans.append(stack[0])
                stack.clear()

            stack.append(i)


        count = 10**4
        for start in ans:
            one = 0
            i, j = start, start + max_len-1
            left, right = s[i], s[j]
            for p in range(i-1, -1, -1):
                if s[p] == left:
                    one += 1
                    left  = '0' if s[p] == '1' else '1'
                else:
                    left = s[p]
            for p in range(j+1, n):
                if s[p] == right:
                    one += 1
                    right  = '0' if s[p] == '1' else '1'
                else:
                    right = s[p]
 
            count = min(count, one)
        
        return count

    # 思路一 数学解法 ： 考虑索引的奇偶性
    def minOperations(self, s: str) -> int:
        one, two = 0, 0 # one ： 奇数是 0 偶数是1， two ： 奇数是 1： 偶数是0
        for i,j in enumerate(s):
            if i%2:
                if j == '0': one += 1
                else: two += 1
            else:
                if j == '1': one += 1
                else: two += 1
        
        return min(one, two)

    # 思路二 动态规划
    def minOperations(self, s: str) -> int:
        n = len(s)
        # dp[i][j] 表示在第i个字符的时候选择的是j状态：0-不交换i字符， 1-交换i字符
        dp = [[0]*2 for i in range(n)]
        # base-case
        dp[0][1] = 1
        dp[0][0] = 0

        for i in range(1, n):
            if s[i] == s[i-1]:
                dp[i][0] = dp[i-1][1]
                dp[i][1] = dp[i-1][0] + 1
            else:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1] + 1

        return min(dp[n-1][0], dp[n-1][1]) 



print(Solution().minOperations("1011101101111011010000110100001000011100101011111011100010111110110101000001101000011111010110011000001111101111011111111001110100011001011101100100110110111010101100111011001101010111010010101100000001100111101010000001010101110110011011010010000110010000011111011100110111000010111110101110010010100011010100010011100010011101011111110001001011000011101000101111111011111101100110011100100100011001101001101111011111110011100111010001000111111111101001111011110011111100101000000000110101110101011001000010110111101101010000111100101101001010110011010001111010110010001111100010000010111001111000000011110011000010011011000011001000000011010101011111011111011101000100100001111110010101011010100010111011101101101010001000010011111010100110101110000101110110100110101010011100"))