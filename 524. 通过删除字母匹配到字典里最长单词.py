class Solution:
    # 回溯 暴力 前缀字符串剪枝
    def findLongestWord(self, s: str, dictionary):
        s = list(s)
        n = len(s)
        d = set(dictionary)
        ans = []
        prefix = set()

        for i in dictionary:
            for j in range(len(i)+1):
                prefix.add(i[:j])
        

        res  = set('')
        max_length = 0

        def back_track(i: int, path, visited):
            nonlocal max_length

            if i == n:
                m = len(max(path, key=lambda x: (x  in d, len(x))))
                if m < max_length:
                    return 
                elif m > max_length:
                    max_length = m
                    res.clear()

                for j in range(len(path)-1, -1, -1):
                    if len(path[j]) == m and path[j] in d:
                        res.add(path[j])

                return
            
            tmp = []
            for string in path:
                if string + s[i] not in prefix:
                    continue
                
                if string + s[i] not in visited:
                    visited.add(string + s[i])
                    tmp.append(string + s[i])
            
            path.extend(tmp)

            # print(path)
            back_track(i+1, path, visited)        

        back_track(0, [''], {''})

        # 字典序最小
        ans = res & set(dictionary)
        return min(ans) if ans else ''