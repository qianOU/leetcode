class Solution:
    def canFormArray(self, arr, pieces) -> bool:
        start = 0
        map_ = {i[0]:j for j, i in enumerate(pieces) if i}
        print(map_)
        n = len(arr)
        while start < n:
            item = arr[start]
            print(item,map_.get(item))
            if map_.get(item) is None:
                return False
            len1 = len(pieces[map_[item]])
            print(start, item, len1, map_)
            if arr[start:start+len1] != pieces[map_[item]]:
                return False
            start = start+len1
        
        return True

print(Solution().canFormArray([85], [[85]]))