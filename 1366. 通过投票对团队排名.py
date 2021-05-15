class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        m, n = len(votes), len(votes[0])
        from collections import defaultdict
        record = defaultdict(lambda : [m]*n)
        
        for i in votes:
            for idx, j in enumerate(i):
                record[j][idx] -= 1
            if len(record[j]) == n:
                record[j].append(j)

        return ''.join(sorted(votes[0], key=lambda x: record[x]))