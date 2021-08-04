def numSpecialEquivGroups( words) -> int:
    def encode(word):
        ans = [0]*52
        for i, w in enumerate(word):
            print(ord(w) - ord('a') + 26*(i%2))
            ans[ord(w) - ord('a') + 26*(i%2)] += 1
        return tuple(ans)
    
    return len({encode(word) for word in words})

print(numSpecialEquivGroups(["abc","acb","bac","bca","cab","cba"]))