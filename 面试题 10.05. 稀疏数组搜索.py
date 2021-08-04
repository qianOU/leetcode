class Solution:
    # 二分
    def findString(self, words: List[str], s: str) -> int:
        def search(l, r):
            print(l ,r)
            if l > r: return -1
            mid = (l + r) // 2
            if words[mid] == s: return mid
            left = right = mid
            # 收缩左边界
            while not words[right] and right <= r:
                right += 1

            while not words[left] and left >= l:
                left -= 1
            
            

            if left >= l:
                if s < words[left]: return search(l, left-1)
                elif s == words[left]: return left         
            if right <= r:
                if s > words[right]: return search(right+1, r)
                elif s == words[right]: return right

            return -1

        return search(0, len(words)-1)