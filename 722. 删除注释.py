class Solution:
    # 双指针
    def removeComments(self, source):
        source[-1] += '\n' # 为了程序的统一
        text = '\n'.join(source)
        text_list = list('\n'.join(source))
        l, r, n = 0, 0, len(text)
        while r < n:
            item = text[r:r+2]
            if item == '//':
                newline = r + text[r:].index('\n')
                text_list[r: newline] = ['']*(newline - r)
                r = newline + 1
                continue
            elif item == '/*':
                idx = r + text[r:].index('*/')
                text_list[r: idx+2] = ['']*(idx + 2 - r)
                r = idx
                continue
            
            r += 1
        return ''.join(text_list).split('\n')[:-1]


print(Solution().removeComments(
["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
))