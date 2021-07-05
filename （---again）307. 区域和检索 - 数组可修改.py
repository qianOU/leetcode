
# 基于数组的线段树（满二叉树）
class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0]*(2*n)
        
        # 满二叉树左右节点的索引是 2*i ， 2*i + 1
        # 自底向上
        for i in range(n, 2*n):
            self.tree[i] = nums[i-n]

        for i in range(n-1, 0, -1):
            self.tree[i] = self.tree[i*2] + self.tree[2*i + 1] # 左 + 右


    def update(self, index: int, val: int) -> None:
        pos = self.n + index # 叶子节点，自底向上，更改 涉及 index 变化的原素
        self.tree[pos] = val
        while pos > 0:
            left = right = pos
            if pos % 2: # 表示 index 是某个节点的右子节点
                left = pos - 1
            else:
                right = pos + 1

            pos //= 2
            # 更改父节点 
            self.tree[pos] = self.tree[left] + self.tree[right]
    

    def sumRange(self, left: int, right: int) -> int:
        l = self.n + left # 定位叶子节点
        r = self.n + right

        ans = 0
        while l < r: # 循环结束的标记就是，l， r 到达了同一个祖先节点, 或者位于两个不同的树上（两个树，l在左子数的右子节点， r 在 右子树 的左子节点上）
             # 如果 l 是 左子树的 右子节点，需要将 l 进位到隔壁子树
             # 因为 父子节点的值，指的是左右子节点的区间和
            if l % 2 == 1:
                ans += self.tree[l]
                l += 1
            if r % 2 == 0: # 如果 r 是右子树的左子节点
                ans += self.tree[r]
                r -= 1
            
            l //= 2
            r //= 2

        # 有公共子区间(子树)的时候 
        if l == r:
            ans +=  self.tree[l]
        return ans  
        

    