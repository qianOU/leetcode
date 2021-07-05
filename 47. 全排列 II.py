class Solution:
    # 回溯 
    # 朴素的思路是利用 visited 数组，以及 将序列编码为字符串进行去重，浪费空间
    # 实际上可以在算法层面实现去重
    def permuteUnique(self, nums):
        ans = []
        n = len(nums)
        visited = set()
        
        encode = lambda x: '-'.join(str(i) for i in x)

        def backtrace(idx, path):
            if idx == n:
                ans.append(path.copy())
                return 

            for i in range(n):
                if nums[i] is not None:
                    # 使用了 nums[i]
                    tmp = nums[i]
                    # 做选择
                    path.append(nums[i])
                    nums[i] = None
                    sign =  encode(path)
                    if sign not in visited:
                        print(sign)
                        visited.add(sign)
                        backtrace(idx+1, path)
                    # 回溯
                    path.pop()
                    nums[i] = tmp

        backtrace(0, [])

        return ans

    # 优化：算法层面去重
    # 首先对nums 数组进行排序，保证了重复元素都是连续的
    # 其后 我们要一定保证每次都是拿从左往右第一个未被填过的数字，
    # [未填入，未填入，未填入] 到 [填入，未填入，未填入]，再到 [填入，填入，未填入]，最后到 [填入，填入，填入] 的过程的，因此可以达到去重的目标。
    def permuteUnique(self, nums):
            ans = []
            n = len(nums)
            vis = [0] * n # 遍历状态数组

            nums.sort()

            def backtrace(idx, path):
                if idx == n:
                    ans.append(path.copy())
                    return 

                for i in range(n):
                    # 如果 nums[i] == nums[i-1] ，并且 i-1 未被遍历过，则是重复状态
                    if i > 0 and nums[i-1] == nums[i] and not vis[i-1]:
                        continue

                    # 如果 i 还没被遍历过
                    if not vis[i]:
                        # 做选择
                        path.append(nums[i])
                        vis[i] = 1

                        backtrace(idx+1, path)

                        # 回溯
                        path.pop()
                        vis[i] = 0

            backtrace(0, [])

            return ans