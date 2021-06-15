class Solution:
    # 错误写法！！！！
    # 找寻 两个 最小的边 a,b 使得 a + b > c（最长边成立即可）
    # 使用二分查找可以加可 找到 c 的速率
    def triangleNumber(self, nums) -> int:
        import collections
        records = collections.defaultdict(int)
        for i in nums:
            records[i] += 1
        
        nums = sorted(records.keys())
        
        print(records, nums)
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                l, r = j, n-1
                # 找到 小于 a+b 的最右侧位置
                target = nums[i] + nums[j]
                while l <= r:
                    mid = l + (r-l) // 2
                    if nums[mid] >= target:
                        r = mid - 1
                    else:
                        l = mid + 1
                
                print('---', i,j, r, ans)
                # 累计结果  
                if j==i:
                    one = records[nums[i]]*(records[nums[i]]-1)//2  
                else:
                    one = records[nums[i]] * records[nums[j]]
                
                # print(i,j,r)
                for ii in range(j, r+1):
                    
                    item = nums[ii]
                    if i==j==ii:
                        if records[nums[j]] >= 3:
                            ans += records[nums[j]]*(records[nums[j]]-1)*(records[nums[j]]-2)//6
                        
                    elif j == ii:
                        if records[nums[j]] >=2:
                            ans += records[nums[i]]*records[nums[j]]*(records[nums[j]]-1)//2
                    else:
                        ans += one*records[item]

                    print(i,j, ii, ans)
                # print(i,j, r, ans)
            
        
        return ans 

print(Solution().triangleNumber(
[2,2,2,3]
))

