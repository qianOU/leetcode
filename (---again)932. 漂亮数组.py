class Solution:
    # 构造题
    # 参考官方： 巧妙的分治
    def beautifulArray(self, n: int) -> List[int]:
        memory = {1: [1]}

        def pair(n): # 表示的是生成 1---n 的漂亮漂亮数组
            if n not in memory:
                left = pair((n+1)//2) # (n + 1) // 2 个奇数
                right = pair(n // 2) # n // 2 个偶数
                # 进行线性变化，对于中点而已，左侧全部为奇数，右侧全部为偶数，即线性变化不会改变漂亮数组性质
                memory[n] = [2*i-1 for i in left] + [2*i for i in right]
            return memory[n]
        
        return pair(n)
