class Solution:
    # 暴力遍历
    def minimumTeachings(self, n: int, languages, friendships) -> int:
        m = len(languages)
        records = {} # 记录的是某一位同学，掌握的语言数
        for i in range(m):
            records[i+1] = set(languages[i])
        
        ans = m
        visited = set() # 记录这个人，是否已经被遍历过也就是 学习了 i 语言
        for i in range(1, n+1):
            res = 0
            visited.clear()
            for p1, p2 in friendships:
                if records[p1] & records[p2]:
                    continue
                for p in [p1, p2]:
                    if i not in records[p] and p not in visited:
                        res +=  1
                        visited.add(p)
                if res >= ans:
                    break
            else:
                ans = min(ans, res)
        
        return ans

    # 贪心算法：
    # 只能选择一门课，那么那门课必须是存在沟通障碍中的入门，最通识的课程，
    # 最少的教学数，就是那些不会这门课程的人数
    def minimumTeachings(self, n: int, languages, friendships) -> int:
        m = len(languages)
        records = {} # 记录的是某一位同学，掌握的语言数
        for i in range(m):
            records[i+1] = set(languages[i])
        
        visited = set()
        from collections import Counter
        a = Counter()
        for p1, p2 in friendships:
            # 如果已经存在一门通用语言的情况
            if records[p1] & records[p2]:
                continue
            for p in [p1, p2]:
                if p not in visited:
                    a += Counter(records[p])
                    visited.add(p)
        print(a)
        # 总人数 - 得到通识教育最多的课程数
        return len(visited) - (a.most_common(1)[0][1] if a else 0)


print(Solution().minimumTeachings(
11
,[[3,11,5,10,1,4,9,7,2,8,6],[5,10,6,4,8,7],[6,11,7,9],[11,10,4],[6,2,8,4,3],[9,2,8,4,6,1,5,7,3,10],[7,5,11,1,3,4],[3,4,11,10,6,2,1,7,5,8,9],[8,6,10,2,3,1,11,5],[5,11,6,4,2]]
,[[7,9],[3,7],[3,4],[2,9],[1,8],[5,9],[8,9],[6,9],[3,5],[4,5],[4,9],[3,6],[1,7],[1,3],[2,8],[2,6],[5,7],[4,6],[5,8],[5,6],[2,7],[4,8],[3,8],[6,8],[2,5],[1,4],[1,9],[1,6],[6,7]]
))