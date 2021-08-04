import random
arr = [4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5]
# arr = arr[:100]
def quick(start, end): # 左闭右开区间
        # print(arr[start:end], start, end)
        if end <= start:
            return 

        k = arr[start] # base 元素
        
        # 左闭右闭区间
        left = start + 1
        right = end - 1
        
        while left <= right:
            while  left < end and arr[left] <= k:
                left += 1

            while right >=0 and arr[right] > k:
                right -= 1

            if left > right:
                break
            
            arr[left], arr[right] = arr[right], arr[left]
  

        arr[start], arr[right] = arr[right], arr[start]

        quick(start, right) 
        quick(left, end)

def quick(left, right): # 左闭右开
            if right <= left:
                return
            k = arr[left]
            l = left + 1
            r = right - 1
            # 搜索区间为左闭右闭
            while l <= r:
                
                while l < right and arr[l] < k:
                    l += 1
                while r >= 0 and arr[r] > k:
                    r -= 1
                if l >= r:
                    break
                
                arr[l], arr[r] = arr[r], arr[l] # 交换之后需要 l， r 移动，不然在面对 arr[l] == arr[r] == k时，会陷入死循环
                l += 1
                r -= 1

            arr[left], arr[r] = arr[r], arr[left]

            quick(left, r)
            quick(l, right)

quick(0, len(arr))
# print(arr)

# 快排 找寻 第 k 小的元素
def quick_select(left, right, k): # 闭区间
    
    idx = random.randint(left, right)
    t = nums[idx]
    # 将 t 交换到最后一个位置
    nums[idx], nums[right] = nums[right], nums[idx]

    l, r = left, right - 1
    while l <= r:
        while l <= r and nums[l] < t:
            l += 1
        
        while l <= r and nums[r] > t:
            r -= 1
        
        if l>=r: break
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l+1, r-1

    # nums[l] 可能大于等于 t
    nums[l], nums[right] = nums[right], nums[l]
    # 查看区间[left...l]是否有k个元素
    if l - left + 1 == k:
        return t
    elif l - left + 1 > k:
        # 在[left, l-1/r] 中寻找 k 个元素
        return quick_select(left, l-1, k)
    else:
        # 在[l+1, right] 找寻 k-(l-left+1) 个元素
        return quick_select(l+1, right, k-(l-left+1))
nums = list([1,2,3])

print(quick_select(0, len(nums)-1, (len(nums)+1)//2+1))


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        from functools import cmp_to_key
        n = len(nums)
        res = [[] for i in range(n)]
        for i in range(n):
            res[i].extend(nums[max(0, i-k):min(n, k+i+1)])
            a = min(res[i], key=cmp_to_key(lambda x, y: abs(x-y)))
            print(res[i], a)
            if a <= t:
                return True
        
        return False

# print(Solution().containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))


# 并查集
class Ufoid:
    def __init__(self, n):
        self.roots = list(range(n))
        self.count = n
    
    def find(self, a):
        while a != self.roots[a]:
            item = self.roots[a]
            self.roots[a]  = self.roots[item] # 压缩路径
            a = self.roots[a]
        return a
    
    def connect(self, a, b):
        return find(a) == find(b)
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return
        elif root_a <= root_b:
            self.roots[root_b] = root_a
        else:
            self.roots[root_a] = root_b
        
        self.count -= 1


num = [1, 2, 10, 1, 5, 10, 3, 3, 7, 2, 14, 14, 7, 7, 2, 6, 0, 1, 9, 2, 2, 3, 5, 4, 1, 5, 4, 6, 1, 14, 0, 6, 
5, 10, 1, 4, 6, 0, 6, 14]
n = len(num)
memory = {}
def dfs(l, r, h):
    if not h:
        return 0
    if memory.get((l, r)):
        return memory[(l, r)]
    hl = num[l-1] if l >0 else 0
    hr = num[r+1] if r<n-1 else 0
    
    left = right = 0
    if  hr:
        right = dfs( l, r+1, min(h, hr))
    if hl:
        left = dfs( l-1, r, min(hl, h))

    ans = max(left, right, h*(r-l+1))
    memory[(l, r)] = ans
    return ans

# for i in range(n):
#     i = 16
#     print(i, dfs(i,i, num[i]))


# 素数删表法
def prime(n):
    for i in range(2, int(n**.5)+1):
        if n % i:
            return False
    return True

def prime_table(n):
    ans = [True]*(n+1)
    for x in range(2, int(n**.5+1)):
        if prime(x):
            for j in range(x**2, n, x):
                ans[x] = False # 素数的倍数，不是素数
    
    # 返回素数的个数
    return sum(ans[2:])

# 背包问题
def solver(n, w, wt, val):
    # dp[i][j] 表示的是 背包容量为 j 的时候，面对 前 i 件物品能获得的最大价值
    dp = [[0]*(w+1) for i in range(n+1)] 
    # base - case
    dp[0][0] = 0 

    for i in range(1, n+1):
        for j in range(1, w+1):
            if j >= wt[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - wt[i-1]] + val[i-1]) # 选 i ，不选 i
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][w]

# 字典树
# 用于字符串匹配
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.chiledren = defaultdict(self.__class__)
        self.ending = False # 表示是否是以该 node 为结尾的单词

class Trie:
    def __init__(self, nums):
        self.root = TrieNode() # 字典树的根节点，只是作为入口
        
    # 将 单词 按招前缀 插入 前缀树中
    def insert(self, word:str):
        cur = self.root
        for w in word:
            cur = cur.chiledren[w]
    
    # 搜寻， 前缀树中 是否 存在 与 word 匹配的单词
    def search(self, word):
        cur = self.root
        flag = True
        for w in word:
            if w not in cur.chiledren:
                flag = False
                break
            cur = cur.chiledren[w]
        
        return flag and cur.ending
    
    # 搜寻：前缀树中是否 存在 prefix 
    def search(self, prefix):
        cur = self.root
        flag = True
        for w in prefix:
            if w not in cur.chiledren:
                flag = False
                break
            cur = cur.chiledren[w]
        
        return flag

## 线段树
# 基于满二叉树的数组实现形式
# 原数组作为叶子节点
# 以求区间和为例子
class NumTree:
    def __init__(self, nums):
        self.n = n = len(nums)
        self.tree = [0]*2*n

        # 放入 树状数组中
        for i in range(n, 2*n):
            self.tree[i] = nums[i-n]
        
        for i in range(n-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1] # 左右子节点的和，形成父节点
        
    
    # 更新原数组 index 的值为 val, 以及其父节点
    def update(self, index, val):
        pos = self.n + index
        self.tree[pos] = val
        
        while pos > 0:
            l = r = pos
            if pos % 2: #如果 pos 是 右子节点(还差左节点，左节点为 pos - 1)
                l = pos - 1
            else: # 如果 pos 是左子节点(还差右节点，右节点为 pos + 1)
                r = pos + 1 
            
            pos //= 2 # 父节点
            self.tree[pos] = self.tree[l] + self.tree[r]


    def sumrange(self, left, right):
        l = self.n + left
        r = self.n + right
        ans = 0
        while l < r:
            if l % 2:
                ans += self.tree[l]
                l += 1
            if r % 2 == 0:
                ans += self.tree[r]
                r -= 1
            # 回溯到根节点
            l //= 2
            r //= 2

        # 回到同一个根节点     
        if l == r:
            ans += self.tree[l]
        
        return ans

# 树状数组\

# 解决区域异或问题
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
    
    def xorrange(self, cur):
        res = 0
        while cur > 0:
            res ^= self.store[cur]
            cur -= cur & -cur
        return res

# 快速乘法模板
def mul(a, b):
    ans = 0
    # 使用的二进制位运算来实现乘法
    while b:
        if b & 1:
            ans += a
        a <<= 1
        b >>= 1
        print(a, b)

    return ans

mul(-3, -1)