class Solution:
    # 贪心 + 单调栈
    def monotoneIncreasingDigits(self, n: int) -> int:
        digit = [int(i) for i in str(n)]
        m = len(digit)
        res = [0]*m
        res[0] = digit[0]
        l = 0
        for i in range(1, m):
            if digit[i] == digit[i-1]:
                continue
            elif digit[i] < digit[i-1]:
                res[l] -= 1
                res[l+1:] = [9]*(m - l - 1) # 余位补 9
                break 
            else:
                res[i] = digit[i]
                l = i
    
        return sum(x*10**i for x, i in zip(res[::-1], range(m)))

print(Solution().monotoneIncreasingDigits(101))