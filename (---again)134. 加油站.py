class Solution:
    # 思路1：暴力 加 剪枝
    # 实际上有更优的算法可以下降到线性复杂度
    def canCompleteCircuit(self, gas, cost) -> int:
        n = len(gas)
        for beg in range(n):
            if gas[beg] < cost[beg]: continue # 如果不满足起点要求
            v = 0
            for j in range(beg, beg+n):
                idx = j%n # 整除可以实现算法的环状遍历
                v += gas[idx] - cost[idx]
                if v < 0:
                    break
            else:
                return beg

    # 数学思维归纳： 假设 x 最后只能到达 y， 则 [x, y]中 的 任何 节点 z 也无法到达 y 之后的加油站
    # 因为 x 能到达 z, 也就说明到达 z 处后，油含量是 大于等于 0的， 之后其不能到达 y 也就说明 z 为起点（油量=0）
    # 的情况下，也是不可能到达 y 之后的下一个加油站的
    # 所以我们可以排除 [x-y] 之间的节点，遍历 y 节点之后的即可
    def canCompleteCircuit(self, gas, cost) -> int:
        n = len(gas)
        x = 0
        while x < n:
            v = 0
            for y in range(x, x+n):
                y = y % n # 构成环状数组
                v += gas[x] - cost[x]
                if v < 0:
                    break
            else:
                return x
            x = y + 1 # 遍历 y 之后的加油站


print(Solution().canCompleteCircuit(
[1,2,3,4,5],
[3,4,5,1,2]
))
        