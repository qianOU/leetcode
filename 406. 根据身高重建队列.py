class Solution:
    # 思路1： 先插入小的再插入大的身高，需要开辟数组来存放，并且需要遍历数组找寻第 i 大的，效率较低
    # 排序规则 ： 身高 升序， k 升序
    def reconstructQueue(self, people):
        n = len(people)
        arr = [float('inf')] * n
        count = list(range(0, n-1))
        people.sort()
        ans = [0]*n

        # print(people)
        for height, order in people:
            total = 0
            for j in range(n):
                if total == order and arr[j] == float('inf'):
                    ans[j] = [height, order]
                    arr[j] = height
                if arr[j] >= height: total += 1
            
            # print(height, order, ans, j)
        
        return ans

    # 排序方法十分重要！！！
    # 思路2：从大到小的身高插入，并且 k 保持升序，使得插入次数减小
    #排序规则  身高减序，k什序
    def reconstructQueue(self, people):
        n = len(people)
        people.sort(key=lambda x:(-x[0], x[1]))
        res = []
        for i,j in people:
            # 如果 i 前面有 j 个比 i 高的， 且 res 长度比 j 小
            if j == len(res): res.append([i, j])
            else: res.insert(j, [i, j])
        return res

print(Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))