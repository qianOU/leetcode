class Solution(object):
    # 使用字典
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        records = dict()
        for i in nums:
            records[i] = records.get(i, 2) - 1
            if records[i] == 0:
                del records[i]
        
        return list(records.keys())[0]

        # 全异或运算
        # 主要使用了异或具有：
        # 1. 交换性质 : a^b^c = a^c^b = c^a^b
        # 2. 异或自身为 0 即 a^a = 0
        # 3. 异或 0 为 自身 即 0^a = a
        def singleNumber(self, nums):
            tmp = 0
            for i in nums:
                tmp ^= i
            return tmp