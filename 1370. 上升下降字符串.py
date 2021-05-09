class Solution:
    def sortString(self, s: str) -> str:
        arr = [0]*26
        for i in s:
            idx = ord(i) - ord('a')
            arr[idx] += 1
        
        ans = []
        while any(i!=0 for i in arr):
            base = ord('a')
            s2 = []
            for i in range(len(arr)):
                if arr[i] > 0:
                    arr[i] -= 1
                    ans.append(chr(base + i))
                
                if arr[i] > 0:
                    arr[i] -= 1
                    s2.append(chr(base + i))
                
            ans.extend(s2[::-1])

        return ''.join(ans)
                