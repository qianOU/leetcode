class Solution:
    # 基于回溯的方法，
    # 重要启示： 不能包含重复，不要思维僵硬只知道 用集合去重， 可以试着在算法层面避免重复！！！！
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        candidates.sort()

        def dfs(i, cur, preselect, path):
            if i == n:
                if cur == target:
                    ans.append(path.copy())
                return 
            
            if candidates[i] + cur <= target:
                path.append(candidates[i])
                dfs(i+1, candidates[i] + cur, True, path)  
                path.pop()
            
            # 代表的是 如果 前一个 元素等于 当前 元素的值， 并且 前一个元素被选中了， 则该元素 没被选择的 路径就不应该被遍历下去
            # 因为 题目 要求解集 不重复， 则 状态 选中 i -- 不选 i+1 和 不选 i ---选i+1 在 两个元素值都相等时，是等价的
            if not(i>0 and candidates[i-1] == candidates[i] and preselect):
                dfs(i+1, cur, False, path)

        
        dfs(0,0, False, [])

        return ans

