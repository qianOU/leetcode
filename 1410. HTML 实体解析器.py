class Solution:
    # 快慢指针
    def entityParser(self, text: str) -> str:
        map_ = {
        "&quot;":'"',
        '&apos;' : "'",
        '&amp;':'&',
        '&gt;': '>',
        '&lt;': '<',
        '&frasl;': '/'
        }
        
        res = list(text)
        slow = fast = 0
        n = len(text)
        while fast < n:
            if text[fast] == '&':
                tmp = fast
                while fast < n and text[fast] != ';':
                    fast += 1

                ans = map_.get(text[tmp:fast+1], text[tmp:fast+1])
                res[slow:slow+len(ans)] = list(ans)
                slow = slow + len(ans)
            else:
                res[slow] = res[fast]
                slow += 1
            
            fast += 1

        return ''.join(res[:slow])

    
    #内置函数
    def entityParser2(self, text: str) -> str:
        
        text = text.replace('&quot;','"')
        text = text.replace('&apos;',"'")
        text = text.replace('&gt;','>')
        text = text.replace('&lt;','<')
        text = text.replace('&frasl;','/')
        text = text.replace('&amp;','&')
        return text

    # 栈方法
    def entityParser(self, text: str) -> str:
        stack = ['']
        cDict = {'&quot;':"\"",'&apos;':'\'','&amp;':'&','&gt;':'>','&lt;':'<','&frasl;':'/'}
        for i in range(0,len(text)):
            if text[i] == '&':
                stack.append('')
            stack[-1] = stack[-1]+text[i]
            if stack[-1][-1] == ';' and stack[-1][0] == '&' :
                if stack[-1] in cDict.keys():
                    stack[-1] = cDict[stack[-1]]
                    stack.append('')
        return "".join(stack)
    
print(Solution().entityParser("&amp;amp;amp;gt;") )
print(Solution().entityParser("&amp;amp;amp;gt;") )