class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ans = [float('-inf')] * 3 # ans 里面存放的就是最大的前三个数
        for i in nums:
            if i > ans[0]:
                ans[0], ans[1], ans[2] = i, ans[0], ans[1]
            elif ans[0]> i >ans[1]:
                ans[1], ans[2] = i, ans[1]
            elif ans[1] > i > ans[2]:
                ans[2] = i
        
        return ans[-1] if ans[-1] != float('-inf') else ans[0]