class Solution:
    # 回溯
    def combine(self, n: int, k: int):
        ans = []
        d = list(range(1, n+1))

        def back_trace(i, s, path):
            if i == k:
                ans.append(path.copy())
                return 
            
            for c in d[s: ]:
                # 剪枝1, 如果剩余元素个数，小于  k个数组合的 剩余个数，则结束
                if k - i > n - c + 1:
                    break
                # 剪枝2： 如果剩余元素个数，正好等于  k个数组合的 剩余个数，则加入答案数组，不再向下回溯
                elif k - i == n - c + 1:
                    tmp = path.copy()
                    tmp.extend(d[c-1:])
                    ans.append(tmp)
                    break
                else:
                    path.append(c)
                    back_trace(i+1, c, path)
                    # 回溯
                    path.pop()
        
        back_trace(0, 0, [])
        return ans


print(Solution().combine(4, 2))

