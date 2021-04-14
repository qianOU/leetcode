class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        if label == 1:
            return [1]
        depth = bin(label) - 3 # 节点位于的树的深度
        pair = 1 << (depth-1)
        ans = [1]
        while pair:
            if pair & label