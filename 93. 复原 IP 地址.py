class Solution:
    # 要用到全部数字，也就是说如果 s 的长度 大于 12 或者 小于 4 直接 放回空列表
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n > 12 or n < 4: return []

        res = []

        def dfs(start, p, path):
            
            if p == 4 and start == n: 
                res.append(path.lstrip('.'))
                return    
        
            # 做选择 当前段最多选择 1 位， 2 位， 3 位 作为 IP 地址的一部分
            for step, left_thr in zip(range(1, 4), (0, 10, 100)):
                if s[start: start + step] and left_thr <= int(s[start: start + step]) <= 255 and p < 4 and start + step <= n:
                    dfs(start + step, p+1, path + '.' + s[start: start + step])
                left_thr = (1 << step - 1)

        dfs(0, 0, '')  
        return res