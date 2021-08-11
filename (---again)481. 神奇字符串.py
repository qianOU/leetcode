class Solution:
    # 模拟，神奇字符串是轮换交替 1， 2 构建 和索引的关系规律
    def magicalString(self, n: int) -> int:
        res = [1,2,2]
        idx = 2
        t = 0
        total = 3
        while total < n:
            t = 1 + t % 2
            for _ in range(res[idx]):
                res.append(t)
            total += res[idx]
            idx += 1

        if total > n: res.pop()
        return sum(i==1 for i in res)
        


