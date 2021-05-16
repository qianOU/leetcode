class Solution:
    # 基于最大堆 + 贪心
    def reorganizeString(self, s: str) -> str:
        from collections import Counter
        a = Counter(s)
        
        from queue import PriorityQueue as PQ
        q = PQ()
        for i, j in a.items():
            q.put((-j, i))
        
        prev = 0
        res = ['']
        while not q.empty():
            # 每次取出 两种不同的字符串进行拼接
            n1, s1 = q.get()
            n1 *= -1
            if q.empty():
                # 如果字符串是奇数的情况之下，只有一种情况扶额和就是多余 的一个字符 与原来拼接的最后一个字符不同
                if n1 == 1 and s1 != res[-1]:
                    res.append(s1)
                    break
                return ''
            n2, s2 = q.get() # n1 大于 n2
            n2 *= -1

            # 和末尾字符进行比较，选择正确的拼接顺序
            if res[-1] != s1:
                res.extend([s1, s2] * n2)
            elif res[-1] != s2:
                res.extend([s2, s1] * n2)
            else:
                return ''
            
            # 将多余的字符重新有序进入优先队列
            if n1 - n2: 
                q.put((n2-n1, s1))

        return ''.join(res[1:])

print(Solution().reorganizeString("snnnnbpnasgowznvnnnlnwhvnnnnfjnnlnnnnnnbnknnqkndzefncknnnnnaiqrntnndnnnjninnnunnunqhndnnqnnsjqnnpiqshntnnncnvnnnncnnqenlnninyndnnnljongnnjwnnnngllnnngkbnllnnnnontlbpngjnnenqnsnnnnnjeqqghnfpngepnodnnnnnnvnsrnughbnipvnhqmnzonoonnnjotnnonoennnpnfnnkdnnbmnmnpnqninnxronnnnvnlanlnnnebnnnlnvnfknsnbincnttnmnguqenhnnxunnnntnnnnhnqnzehvunfnvnndvnjnnnbnnpxnqipwnmnonnndlnsnonnninnxnnnjnnnnnesennmyiednnnnnnnnnhimtnnnonjlicnwnwvnntaxmnrntnnnnsnbnanninnecbcfjxncnnkvnnqgnunensanpnngjnzxjnopnnyvnnxskniyytnsnnnnx"))