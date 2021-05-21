class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        n = len(prerequisites)
        if not n:
            return True

        from collections import defaultdict
        records = defaultdict(list)
        visited = [True] * numCourses
        for j, i in prerequisites:
            records[i].append(j)
            visited[i] = visited[j] = False


        def dfs(i, visited):
            print(i)
            if all(visited) and not records.get(i):
                print(visited, i)
                return True
            
            ans = []

            for tmp in records[i]:
                if not visited[tmp]:
                    visited[tmp] = True
                    ans.append(tmp)
                else:
                    return False
            return all(dfs(i, visited) for i in ans)
                    

        print(records)
        for i in range(n):
            visited1 = visited
            visited1[prerequisites[i][-1]] = True
            if dfs(prerequisites[i][-1], visited1):
                return True

        return False

print(Solution().canFinish(
5,
[[1,4],[2,4],[3,1],[3,2]]))