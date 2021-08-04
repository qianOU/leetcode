class Solution:
    # 解法1： 树状数组
    def xorQueries(self, arr, queries):
        class BIT:
            def __init__(self, nums):
                self.n = len(nums)
                self.store = [0]*(1+self.n) # 树状数组真实有效的索引从 1 开始
                for i in range(1, 1+self.n):
                    self.update(i, nums[i-1])
            
            def update(self, idx, val):
                while idx <= self.n:
                    self.store[idx] ^= val
                    idx += idx & -idx
            
            def sumrange(self, cur):
                res = 0
                while cur > 0:
                    res ^= self.store[cur]
                    cur -= cur & -cur
                return res
        
        bit = BIT(arr)
        ans = []
        for i, j in queries:
            ans.append(bit.sumrange(j+1) ^ bit.sumrange(i))
        return ans
    
    # 解法二 前缀异或值
    def xorQueries(self, arr, queries):
        acc = list(accumulate([0] + arr, xor))
        return [acc[i] ^ acc[j+1] for i, j in queries]
    
    # 解法3： 线段树
    def xorQueries(self, arr, queries):
        class NumTree:
            def __init__(self, nums):
                self.n = n = len(nums)
                self.nums = [0]*2*n # 完全二叉树（索引位置为0的空出来）
                
                # 叶子节点赋值
                for i in range(n, 2*n):
                    self.nums[i] ^= nums[i-n]
                # 父亲节点赋值
                for i in range(n-1, 0, -1):
                    # 索引关系构建左子树与右子数
                    self.nums[i] = self.nums[2*i] ^ self.nums[2*i+1]


            def update(self, idx, val):
                pos =  self.n + idx
                self.nums[pos] = val
                while pos > 0: # 更新是从叶子节点，一直更新回溯到根节点
                    l = r = pos
                    if pos % 2: l = pos - 1 # 如果 pos 是右子节点(还差左节点，左节点为 pos - 1)
                    else: r = pos + 1  # 如果 pos 是左子节点(还差右节点，右节点为 pos + 1)

                    pos //= 2
                    self.nums[pos] = self.nums[l] ^ self.nums[r]
            
            def xorange(self, left, right):
                l = self.n + left
                r = self.n + right
                res = 0
                while l < r:
                    if l % 2: 
                        res ^= self.nums[l]
                        l += 1
                    if r%2 == 0:
                        res ^= self.nums[r]
                        r -= 1
                    # 回溯到根节点
                    l //= 2
                    r //= 2

                # 如果回到了同一个根节点
                if l == r: res ^= self.nums[l]

                return res
        
        numtree = NumTree(arr)
        print(numtree.nums)
        ans = []
        for i, j in queries:
            ans.append(numtree.xorange(i, j))
        return ans

print(Solution().xorQueries([1,3,4,8],
[[0,1],[1,2],[0,3],[3,3]]))