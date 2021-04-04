class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        map_ = dict(zip("type color name".split(), range(3)))
        col = map_[ruleKey]
        return [item[col] for item in items].count(ruleValue)