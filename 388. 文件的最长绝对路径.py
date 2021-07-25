class Solution:
    def lengthLongestPath(self, input: str) -> int:
        from collections import deque
        import re
        q = deque([(input, 0)])
        ans = 0
        layer = 0
        while q:
            sz = len(q)
            layer += 1
            for _ in range(sz):
                path, k = q.popleft()
                k += 1
                nxts = re.split(r'\n' + r'\t'*layer + r'(?!\t)', path)
                k += len(nxts[0])
                if len(nxts) == 1:
                    ans = max(ans, k)
                else:
                    for next in nxts[1:]:
                        q.append((next, k))
        return ans - 1


print(Solution().lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))