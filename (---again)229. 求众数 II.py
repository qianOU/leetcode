class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_1 = count_2 = 0
        # 在配对 抵消的过程中， num1 与 num2 是不相同的元素
        num1 = num2 = None
        for i in nums:
            if i == num1:
                count_1 += 1
                continue

            if i == num2:
                count_2 += 1
                continue

            if not count_1:
                num1 = i
                count_1 += 1
                continue

            if not count_2:
                num2 = i
                count_2 += 1
                continue

            # 如果 i  既不与 num1 也不与 num2 相等，则进行抵消
            count_1 -= 1
            count_2 -= 1


        # 校验阶段
        res = []
        for item in [num1, num2]:
            ans = 0
            for j in nums:
                ans += j == item
            if ans > len(nums)//3:
                res.append(item)
        
        return res

