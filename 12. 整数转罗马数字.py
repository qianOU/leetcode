class Solution:
    # 贪心最大值匹配
    def intToRoman(self, num: int) -> str:
        keys = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        map_ = dict(zip(
                    keys,
                    ['I', 'IV','V', 'IX' ,'X','XL', 'L',  'XC', 'C', 'CD', 'D', 'CM', 'M']
               ))

        n, res = len(keys) - 1, ''
        while num:
            l, r = 0, n
            # 找到小于等于 num 的第一个数
            while l <= r:
                mid = (l + r) >> 1
                if keys[mid] <= num:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            # （优化点）查看倍数关系，减少 二分查找的次数
            times = num //  keys[r]   
            res += map_[keys[r]] * times
            num -= keys[r] * times

            # （优化）缩小二分查找范围
            n = r - 1 

        return res


print(Solution().intToRoman(3999))