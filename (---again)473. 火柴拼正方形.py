class Solution:
    # 思路一：回溯， 需要使用一个 长度为4 的列表，表示装载四条边的四个容器
    def makesquare(self, matchsticks) -> bool:
        if not matchsticks:
            return False

        total = sum(matchsticks)
        if total % 4:
            return False

        length = total // 4
        n = len(matchsticks)

        matchsticks.sort(reverse=True) # 从大到小放入，四条边中，便于尽快发现不合适的进行剪枝
        contain = [[] for i in range(4)]

        def back(i): # i表示当前搜索状态
            if i == n:
                return sum(contain[0]) == sum(contain[1]) == sum(contain[2]) == sum(contain[3]) == length

            for j in range(4):# 尝试将 i 放入 j 边中
                if sum(contain[j]) + matchsticks[i] <= length:
                    contain[j].append(matchsticks[i])
                    if back(i+1):
                        return True
                    # 回溯
                    contain[j].pop()

            return False
        
        return back(0)


print(Solution().makesquare([5,5,5,5,4,4,4,4,3,3,3,3]))