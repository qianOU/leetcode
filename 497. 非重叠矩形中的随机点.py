import random
class Solution:
    # 注意是非重叠的矩形,可以转换为累计概率分布，将矩形x的跨库作为一部分
    def __init__(self, rects):
        self.cdf = [0] # 累计概率分布函数,单调递增特性
        self.num = len(rects)
        self.rects = rects
        for x1, y1, x2, y2 in rects:
            self.cdf.append(self.cdf[-1] + (x2 - x1 + 1)*(y2-y1 + 1))
        self.total = [0]*self.num 
    def pick(self):
        item = random.randint(1, self.cdf[-1]) # 在左开右闭区间进行抽取,所以最小值是1
        l, r = 0, self.num
        while l <= r: # 找寻的是大于等于 idx 的第一个元素索引位置
            mid = (l + r) // 2
            if self.cdf[mid] >= item: r = mid - 1
            else: l = mid + 1
        rectangle = self.rects[r]
        self.total[r] += 1
        print((item - self.cdf[r]))
        return [(item - self.cdf[r] - 1) // (rectangle[3] - rectangle[1] + 1) + rectangle[0],
                (item - self.cdf[r] - 1) % (rectangle[3] - rectangle[1] + 1) + rectangle[1]]

# Your Solution object will be instantiated and called as such:
obj = Solution([[-2,-2,1,1],[2,2,4,6]])
for i in range(3):
    (obj.pick())

print(obj.total)
