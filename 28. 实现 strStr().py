class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 得到 Next数组
        def getNext(patten):
            n = len(patten)
            next = [-1] * n
            # base case
            next[0] = -1
            # next[1] = 0 # 则是循环触发的第一步
            i, j = 0, -1 # 主字符串的指针i, 模式字符串的指针 j

            while i < n - 1:
                # 以nums[i] 为结尾的 子串的 PMT值
                if j == -1 or patten[i] == patten[j]:
                    i += 1
                    j += 1
                    next[i] = j

                else: # 不匹配的话.回退模式串的指针
                    j = next[j]

            return next

        # KMP算法
        def KMP(main, patten):
            m, n = len(main), len(patten)
            if not n: return 0
            next = getNext(patten) # next 数组
            i, j = 0, 0 

            while i < m and j < n:
                if j == -1 or main[i] == patten[j]:
                    i += 1
                    j += 1
                else: # 回退模式串指针
                    j = next[j]
            
            # 匹配的字符串区间是[i-j, i-1]
            if j == n: return i - j
            return -1
                

        return KMP(haystack, needle)

