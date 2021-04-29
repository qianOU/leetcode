class Solution:
    def simplifyPath(self, path: str) -> str:
        cur = ['']
        items = path.split('/')

        for i in items:
            if i:
                if len(cur)>1 and i == '..':
                    cur.pop()
                elif i != '.':
                    cur.append(i)

        return '/'.join(cur)