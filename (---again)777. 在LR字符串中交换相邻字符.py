class Solution:
    # 双指针问题
    # 两个点
    # tips 1: L, R 的相对顺序是不会改变的，L, R 是不会交叉的
    # tips 2：L 只能向左移动， R 只能向右移动，说明 在 start 中 L 的索引位置大于等于 end， R 是小于等于 end
    def canTransform(self, start: str, end: str) -> bool:
        m, n = len(start), len(end)
        if m != n: return False
        i, j = 0, 0 # 双指针
        while i < n and j < n:
            while i < n and start[i] == 'X': i += 1
            while j < n and end[j] == 'X': j += 1

            if i >= n or j >= n: break
            if start[i] != end[j]: return False
            elif start[i] == 'L' and i < j: return False
            elif start[i] == 'R' and i > j: return False
            
            i, j = i + 1, j + 1
        
        # 尾指针进行处理,查看是否尾部只是X了
        return not (start[i:].strip('X') or end[j:].strip('X'))
            
        
