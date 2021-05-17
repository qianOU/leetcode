


class Solution:
    # 最优方法 ： 利用 i + j = k 值， 并且 每一层扫描的 k 是递增的来处理
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        from collections import defaultdict
        a = defaultdict(list)
        for i in range(len(m-1), -1, -1): # 从最后一行开始烧苗确保有序
            for j in range(len(nums[i])):
                a[i+j].append(nums[i][j])
        
        # 从小到大排序 i+j 的值，达到符合要求的目的
        res = []
        for i in sorted(a):
            res.append(a[i])
        return res


    # 方法1： （超时）暴力扫描
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m, n = len(nums), len(max(nums, key=len))

        ans = []
        for k in range(0, 2*max(m, n)):
            for i in range(k, -1, -1):
                j = k - i
                if i >= m:
                    continue 
                if  0<= j < len(nums[i]):
                    ans.append(nums[i][j])
        
        return ans
    
    # 方法二 BFS 每次走一步
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        from collections import deque

        m = len(nums)
        q = deque([(0, 0)])
        len_arr = [len(i) for i in nums]
        
        ans = []
        visited = set((0, 0)) # 是否遍历过的集合
        while q:
            sz = len(q)
            for _ in range(sz): # 每一层 对应 与 1 条斜线
                item = q.popleft()
                ans.append(nums[item[0]][item[1]])
                if item[1] >= len_arr[item[0]]: # 如果 长度越界则循判断下一个元素
                    continue
                # 上三角部分 : 优先 下方元素入队列，其次是 右方元素
                if item[0] + 1 < m and len_arr[item[0]+1] > item[1]: #确定 下方存在这样的元素
                    if  (item[0]+1, item[1]) not in visited:  
                        q.append((item[0]+1, item[1]))
                        visited.add((item[0]+1, item[1]))
                
                # 如果是 下三角部分：则 只能 右方元素入队列
                if item[1] + 1 < len_arr[item[0]]: 
                    if (item[0], item[1]+1) not in  visited:
                        q.append((item[0], item[1]+1))
                        visited.add((item[0], item[1]+1))
        
        return ans