class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            stack = []
            for i in s:
                if stack and i == '#':
                    stack.pop()
                elif i != '#':
                    stack.append(i)
            return stack
        # print(build(s) , build(t))
        return build(s) == build(t)

print(Solution().backspaceCompare("y#fo##f",
"y#f#o##f"))