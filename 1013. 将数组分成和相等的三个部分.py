class Solution:
    def canThreePartsEqualSum(self, arr) -> bool:
        total = sum(arr)
        n = len(arr)
        if total % 3: return False
        mdu = total // 3
        sum_ = 0
        count = 2
        for i in range(n):
            sum_ += arr[i]
            if sum_ == mdu:
                sum_ = 0
                count -= 1
                if not count: return True


print(Solution().canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))