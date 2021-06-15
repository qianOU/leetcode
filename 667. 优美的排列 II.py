class Solution:
  
    def constructArray(self, n: int, k: int):
        l, r = 1, n
        count = 0
        ans = []

        while len(ans) <  k:
            ans.append(r)
            r -= 1
            # 如果 第 k 个元素是 右指针， 则剩下的需要递减顺序放入
            if len(ans) == k:
                ans.extend(range(r, l-1, -1))
                return ans
            ans.append(l)
            l += 1
        # 如果 第 k 个元素是 左指针， 则剩下的需要递增顺序放入
        ans.extend(range(l ,r+1))
        return ans

print(Solution().constructArray(10, 3))