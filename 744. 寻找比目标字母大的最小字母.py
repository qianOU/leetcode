class Solution(object):
    # 暴力 
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        ans = letters[0]
        s = f = 0
        while f < len(letters):
            if letters[s]<=target<letters[f]:
                break
            s = f
            f += 1
        
        return letters[f%len(letters)] 
    
    # 提供的是有序数组，所以可以 使用 二分搜索
    def nextGreatestLetter(self, letters, target):
        left = 0
        right = len(letters) - 1
        while left <= right: # 找寻右边界
            mid = left + int((right-left)/2)
            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1  # 搜寻右边界，所以需要固定右边界，缩 左边界

        print(left, right)
        # 太冗余
        # return letters[0] if right >=len(letters)-1 else letters[right+1] 
        # 记得退出循环的时候是 left = right + 1
        # right 是 等于 target 的右边界， 所以 left 就是比 target 大的元素下标
        # 而 right == len(letters) - 1 也就表示 letters 中任何字符都比 target 小
        # 此时 需要返回首元素 0 ， 也就是为 left % len
        return letters[left % len(letters)]


print(Solution().nextGreatestLetter(["c", "f", "j"], 'a'))


