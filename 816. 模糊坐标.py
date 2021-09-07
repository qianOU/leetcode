class Solution:
    # 回溯
    def ambiguousCoordinates(self, s: str):
        ans = []
        n = len(s)
        def helper(one):
            l, n = 0, len(one)
            tmp = []
            if n == 1 or one[0] != '0': tmp = [one]
            for l in range(n-1): # 遍历的小数点位置在 l 后
                left, right = one[:l+1], one[l+1:]
                if l > 0 and left[0] == '0': break
                if  right[-1] == '0': break
                tmp.append(left + '.' + right)

            return tmp

        # 遍历分割位置
        for i in range(2, n-1):
            pre, behind = helper(s[1:i]), helper(s[i:-1])
            for i in pre:
                for j in behind:
                    ans.append('(%s, %s)' % (i, j))
        
        return ans

print(Solution().ambiguousCoordinates("(0010)"))