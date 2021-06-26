class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 二进制中，某个 位置 i ，如果是 出现了3次的那个数字，则在那个位置上 1 的个数一定可以被 3 整除
        # 最后 i 的位置上 %3 余的就是单独元素 在 i 处二进制的数字
        ans = 0
        for i in range(32): 
            # 二进制中 第 i 位数字和
            total = sum((j>>i)&1 for j in range(nums))
            # 由于 python 中， 整形 没有 有无 符号之分，所以需要手动更改
            if total % 3:
                if i == 31：
                    ans -= 1 << i
                else:
                    ans |= 1 << i
            
            return ans