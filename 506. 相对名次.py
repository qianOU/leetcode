class Solution:
    def findRelativeRanks(self, score):
        paiming =  ["Gold Medal", "Silver Medal", "Bronze Medal", *[str(i) for i in range(4, len(score)+1)]]
        ans = sorted([list(i) for i in zip(score, range(len(score)))], reverse=True)
        for i in range(len(ans)):
            ans[i][0] = paiming[i]
        return [i[0] for i in sorted(ans, key=lambda x:x[1])] 

    def findRelativeRanks(self, score):
        rank_dic = {score: rank+1 for rank,score in enumerate(score)}
        map_ = dict(zip(range(1,4), ["Gold Medal", "Silver Medal", "Bronze Medal"]))
        return [map_.get(rank_dic[i], str(rank_dic[i])) for i in score]

print(Solution().findRelativeRanks([2,4,3,5,1]))