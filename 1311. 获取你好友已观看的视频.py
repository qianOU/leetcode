class Solution:
    def watchedVideosByFriends(self, watchedVideos, friends, id: int, level: int) :
        n = len(watchedVideos)
        adj = friends
        print(adj) 
        from collections import deque
        q = deque()
        q.append(id)
        visited = set([id])

        count = 0
        ans = []
        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                print(count, cur)
                if count == level:
                    ans.append(cur)
                    continue
                for j in adj[cur]:
                    if j not in visited:
                        visited.add(j)
                        q.append(j)
            
            count += 1

            if count > level:
                break
        
        from itertools import chain
        res =[i for i in chain(*[watchedVideos[i] for i in ans])]
        ans = sorted(set(res), key=lambda x:(res.count(x), x))
        return ans
        

print(Solution().watchedVideosByFriends(
[["m"],["xaqhyop","lhvh"]],
[[1],[0]],
1,
1


))