class Solution:
    # 对于这种螺旋填充数组，都是需要分层处理
    # 按圈数进行处理
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        code = lambda x: x%9 if x % 9 else 9 # 转换坐标函数
        cur = min(xPos, yPos, num-xPos-1, num-yPos-1) + 1 # 当前所处的圈数，从 1 开始计数
        # 当前圈的长度
        len = num - 2*(cur - 1)
        # 头顶点坐标
        head_r, head_c = cur - 1, cur - 1
        total = num * num  # 所有的元素数量
        if xPos <= yPos: # 如果在的右上角
            return code((total - len*len + (yPos - head_r) + (xPos - head_c) + 1))
        else: # 采取回撤 m 步的做法
            return code((total - (len-2)*(len-2) - ((xPos - head_c) + (yPos - head_r) - 1)))
