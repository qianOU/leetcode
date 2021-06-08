class Solution:
    # 这类题 就是模拟，将牌组设置为双端队列
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        from collections import deque
        n = len(deck)
        q = deque(range(n)) # 双端序列里面存放的是牌组索引，模拟的是牌组规则
        ans = [None]*n

        for card in sorted(deck):  
            ans[q.popleft()] = card # 抽出牌顶的牌
            if q: # 如果还有牌
                q.append(q.popleft()) # 将牌顶的牌放到底部
        
        return ans