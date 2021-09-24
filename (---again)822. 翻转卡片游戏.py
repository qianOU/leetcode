class Solution:
    # hash表, 如果卡牌两侧数字都一致的话，是无效翻转，不一致的卡牌里面每一面的值都有可能是解
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(backs)
        same = {i for i, j in zip(fronts, backs) if i == j}
        ans = float('inf')
        for i in itertools.chain(fronts, backs):
            if i not in same: ans = min(ans, i)
        return ans if ans < float('inf') else 0