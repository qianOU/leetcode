class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        mid = n // 2 if n%2 ==0 else (n+1) // 2
        res = nums.copy()

        for i in range(1, n, 2):
            nums[i] = res[n  - (i+1)//2]
        for i in range(0, n, 2):
            nums[i] = res[mid-1 + i//2]

        return nums

print(Solution().wiggleSort([4,5,5,6]))


