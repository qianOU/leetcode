class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        p = len(s)
        ans = []
        item = ''
        one = 0
        while p>=0:
            if s[p] == '-':
                p -= 1
                continue

            one += 1
            item = s[p] + item
            if one%k==0:
                
                ans.append(item.upper())
                item = ''
            p-=1
        
        if one%k:
            ans.append(item.upper())
        
        return '-'.join(ans[::-1])