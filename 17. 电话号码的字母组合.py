class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        records = {'2':'abc','3':'def','4':'ghi','5':'jkl', '6':'mno',
        '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if not digits:
            return []
        ans = []
        n = len(digits)

        def dfs(i, path):
            if i == n:
                ans.append(path)
                return
            for j in records.get(digits[i], ''):
                dfs(i+1, path+j)
        
        dfs(0)

        return ans

        