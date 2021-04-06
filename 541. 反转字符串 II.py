class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        aaa = []
        slow = fast = 0
        while fast < n:
            if (fast + 1)%(2*k) == 0:
                aaa.append(s[slow: slow+k][::-1])
                aaa.append(s[slow+k, slow+2*k])  
                slow = fast + 1
            fast += 1
        
        aaa.append(s[slow:slow+k][::-1])
        if fast - slow > k:
            aaa.append(s[slow+k:fast])

        return ''.join(aaa)

print(Solution().reverseStr())