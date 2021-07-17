class Solution:
    def verifyPostorder(self, postorder) -> bool:
        n, left, right = len(postorder), float('-inf'), float('inf')
        
        v2idx = {j: i  for i,j in enumerate(postorder)}

        def helper(lb, rb, left, right): # 闭区间
        
            if left > right: return False
            if lb > rb: return True

            center = postorder[rb]
            
            if  center <= left or  center >= right: return False
            # 确定左子节点， 最后一个 小于 根节点的元素
            l, r = lb, rb - 1
            while l <= r:
                mid = (l + r) >> 1
                if postorder[mid] >= center:
                    r = mid - 1
                else:
                    l = mid + 1
           
            print(postorder[lb],  postorder[rb],   postorder[r], left, right, center)
            

            if r < lb:
                return helper(lb, rb-1, center, right)

            return (left < postorder[r] < center) and helper(r+1, rb-1, center, right) and \
             helper(lb, r, left, center)
        
        return helper(0, n-1, left, right)


print(Solution().verifyPostorder(
[1,2,5,10,6,9,4,3]))