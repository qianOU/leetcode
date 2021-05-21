class Solution:
    # 堆房子 要求 同一层相邻的两块砖头 必须有共工支撑点
    # 常规的暴力 破解
    def pyramidTransition(self, bottom: str, allowed) -> bool:
        n = len(allowed)

        from collections import defaultdict
        records = defaultdict(list)
        for idx, i in enumerate(allowed):
            records[i[:2]].append(i[-1])

        # 记录当前所有可能的上一层 字符索引
        all_path = []
        def helper(string, i, n, path):
            if i==n:
                all_path.append(path)
                return 
            if string[i-1: i+1] in records:
                helper(string, i+1, n, path+[i+1])
            
            # 不合理的考虑， 两块砖头中间必须有公共支撑点作为桥梁
            # if string[i:i+2] in records:
            #     helper(string, i+2, n, path + [i+2])


        def dfs(cur):
            if  len(cur) == 1:
                return True
            elif len(cur) == 2:
                return cur in records
            n = len(cur)
            # 得到所有可能的上层字符串
            helper(cur, 2, n, [2])
            print(all_path)
            ans = []
            for item in all_path:
                if item[-1] != n:
                    continue
                
                for tmp in records[cur[:2]]:
                    prev = item[0]
                    for i in range(1, len(item)):
                        # 多余考虑 堆砖的要求就是必须要有公共点
                        # if item[i] - prev > 1:
                        #     tmp = [string + j for string in tmp  for j in records[cur[prev:item[i]]]]
                        if item[i] - prev == 1:
                            tmp = [string + j  for string in tmp for j in records[cur[prev-1:item[i]]]]
                        prev = item[i]
                    ans.append(tmp)
        
            tmp = []
            for i in ans:
                tmp.extend(i)
            for string in tmp:
                if dfs(string):
                    return True
                # 每次 经过一次 dfs 需要置空 all_path 数组， 因为 里面调用了 helper
                all_path.clear()

        return bool(dfs(bottom))