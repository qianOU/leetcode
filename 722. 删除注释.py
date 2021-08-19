class Solution:
    # 双指针
    def removeComments(self, source):
        text = '\n'.join(source)
        l = r = 0
        n, sign = len(text), ''
        left = -1
        right = 0
        res = []
        while r <= n:
            if r < n and not sign and (text[r:r+2] == '//' or text[r:r+2] == '/*'):
                if right:
                    if res[-1] + text[right:r]:
                        res[-1] += text[right:r]
                    else: res.pop()
                    right = 0

                left = r
                sign = text[r:r+2]
                r += 2
                continue
            if r == n or text[r] == '\n':
                if not sign and not right:
                    res.append(text[l:r])
                elif sign == '//':
                    if not right:
                        if text[l:left]:
                            res.append(text[l:left])
                    else:
                        if res[-1] + text[right:r]:
                            res[-1] += text[right:r]
                        else: res.pop()
                        right = 0
                    
                    sign = ''

                if not right and sign == '':
                    l = r + 1
            
            elif r < n and sign == '/*' and text[r:r+2] == '*/':
                sign = ''
                res.append(text[l:left])
                right = l = r + 2
            
            r += 1
        
        return res


print(Solution().removeComments(
["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
))