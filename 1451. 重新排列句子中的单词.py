class Solution:
    def arrangeWords(self, text: str) -> str:
        ans = sorted(text.lower().split(), key=len)
        if not ans:
            return ''
        ans[0]= ans[0].capitalize()
        
        return ' '.join(ans)