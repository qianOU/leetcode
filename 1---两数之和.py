class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        # 类似于 备忘录
        quire = dict()

        # 由于是遍历了数组，所以构建target的两个元素都是不同的（索引位置不同）
        for i in range(len(nums)):
            # 如果 与 nums[i] 匹配的值已经 被记录了，也就找到了解
            if quire.get(target-nums[i]) is not None:
                return [ quire.get(target-nums[i]), i]
            quire[nums[i]] = i
        


if __name__ == "__main__":
    ans = Solution()
    re = ans.twoSum([3,3], 6)
    print(re)