class Solution:
    # 因为斐波那契既有偶数2 也有 奇数 1，所以只需要考虑最近的 偶数 和奇数即可
    def findMinFibonacciNumbers(self, k: int) -> int:
        # 最少次数 BFS
        import functools, bisect
        @functools.lru_cache(None)
        def fibo(x): 
            return 1 if x<=2 else fibo(x-1) + fibo(x-2)

        ans = [] # 有序, 可以使用二分搜索 来剪枝
        for i in range(1, 10**5):
            item = fibo(i)
            if item > k: break
            ans.append(item)
        
        from collections import deque

        q = deque([k])
        n = len(ans)
        visited = set() # 剪枝
        visited.add(k)
        count = 0
        flag = 0 # 如果找到了一个解 就设置为 1
        while q:
            sz = len(q)
            for _ in range(sz):
                item = q.popleft()
                #二分查找下一个元素
                
                idx = bisect.bisect_left(ans, item)

                if 0<=idx<n and item == ans[idx]:
                    flag = 1
                    break
                # 因为斐波那契数列 注定了 每 三个数 就有2个奇数 ，一个偶数的性质
                for i in range(idx-1, max(idx-4, 0), -1):
                    if item - ans[i] not in visited:
                        q.append(item - ans[i])
                        visited.add(item - ans[i])

            count += 1

            if flag:
                break
        
        return count

print(Solution().findMinFibonacciNumbers(9))