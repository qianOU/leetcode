class Solution:
    # 分治，如果 s 中某些字符计数本身就小于 k，则这些字符只能作为分隔符存在,剩下的就是子问题了
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k: return 0
        counter = Counter(s)
        for i, v in counter.items():
            if v < k:
                return max(self.longestSubstring(s1, k) for s1 in s.split(i))
        return  len(s)
    
    # 滑动窗口，通过追加限制条件使得滑动窗口的滑动知道何时停止（），以及收缩窗口，最后对追加的限制的条件下的解，求最大值即可
    def longestSubstring(self, s: str, k: int) -> int:
        s = list(s)
        n = len(s)
        ans = 0
        # 追加限制条件，限制窗口中字符的种类
        for p in range(1, 27):
            left = right = 0
            window = 0 # 记录的是窗口字符种类
            leng = 0 # 达标的字符的计数
            # 字符的计数数组
            counter  = [0]*26

            flag = 1 # 是否需要遍历更多的字符情况
            while right < n:
                idx = ord(s[right]) - ord('a')
                counter[idx] += 1
                if counter[idx] == 1: window += 1
                if counter[idx] == k: leng += 1

                # 如果窗口出现的字符类型，多余指定的时候，需要收缩左边界
                while window > p:
                    idx = ord(s[left]) - ord('a')
                    counter[idx] -= 1
                    if counter[idx] == 0: window -= 1
                    if counter[idx] == k-1: leng -= 1

                    left += 1 # 收缩左指针

                if window == leng: # 如果窗口出现的字符种类数，和达标的种类数一致的时候
                    flag = 0
                    ans = max(ans, right - left + 1)
                
                right += 1
            
            # 如果在 p 的时候，没有符合  window == leng 的情况，则之后的 p 都不需要遍历
            if flag: break

        return ans

