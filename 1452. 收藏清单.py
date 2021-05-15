class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        fav = [frozenset(i) for i in favoriteCompanies]
        ans = []
        for idx, i in enumerate(favoriteCompanies):
            if any(frozenset(i).issubset(j) for ii, j in enumerate(fav) if ii != idx):
                continue
            ans.append(idx)
        return ans