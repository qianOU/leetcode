class Solution:
    def freqAlphabets(self, s: str) -> str:
        map_ = dict(zip([str(i) for i in range(1, 10)],[chr(i) for i in range(ord('a'), ord('a')+9)]))
        map_.update(dict(zip([str(i)+'#' for i in range(10 ,27)],
        [[chr(i) for i in range(ord('j'), ord('j')+17)]])))
        p = 0
        ans = []
        n = len(s)
        while p < n:
            tmp = map_.get(s[p:p+3])
            if tmp:
                ans.append(tmp)
                p += 3
            else:
                ans.append(map_.get(p))
                p+=1
        
        return ''.join(ans)