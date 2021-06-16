class Solution:
    def canChoose(self, groups, nums) -> bool:
        n1 = len(groups)
        pl = 0

        l, n = 0, len(nums)
        while l < n:
            if pl == n1:
                return True
            
            k1= len(groups[pl])
            if nums[l:l+k1] == groups[pl]:
                pl += 1
                l = l + k1
            else:
                l += 1
            print(l ,pl)
        return pl == n1


print(Solution().canChoose(
[[9099312,-7882487,-1441304,6624042,-6043305]],
[-1441304,9099312,-7882487,-1441304,6624042,-6043305,-1441304]

))