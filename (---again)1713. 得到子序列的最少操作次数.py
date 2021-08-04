class Solution:
    # 求最少操作次数，也就是找寻 最长公共子序列问题
    # 时间复炸度为 0(nlogn)
    # 思维方式： 最长公共子序列问题 --->（由于target数组元素是各不相同的） 最长递增子序列问题
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        m, n = len(target), len(arr)
        dic = {target[i]: i for i in range(m)}
        ans = [] # ans[i] 表示的是长度为 i 的 LIS 的最小的索引， ans 是递增的
        # 构造 res 数组的步骤可以被省略
        # 只获取arr中含有 target 的元素
        # res = [dic[i] for i in arr if dic.get(i) is not None]
        # # 求 res 的 LIS （ps 因为 target 的索引是从小到大排列的）
        # for i in res:
        for v in arr:
            # 跳过不在 target 中的元素
            if v not in dic: 
                continue

            i = dic[v] # 转换为索引
            if not ans or ans[-1] < i:
                ans.append(i)
                continue
            # 二分查找大于等于 i 的最左侧元素,表示构成 其长度的最小元素更新为 i
            l, r = 0, len(ans) - 1
            while l <= r:
                mid = (l + r) // 2
                if ans[mid] >= i:
                    r = mid - 1
                else: l = mid + 1
            if l == len(ans):
                ans.append(i)
            else:
                ans[l] = i
        
        return m - len(ans) 
