class Solution(object):
    #递归
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        rows = len(image)
        cols = len(image[0])
        # 方向数组
        d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()
        visited.add((sr, sc))
        start = image[sr][sc]

        def backtrace(image, sr, sc):
            # 当层决策
            image[sr][sc] =  newColor
            # 选择列表
            for i, j in d:
                x = sr + i
                y = sc + j

                # 排除 不合法的 选择
                if x <0 or x >= rows:
                    continue 
                if y<0 or y >=  cols:
                    continue
                if image[x][y] != start:
                    continue
                if (x, y) in visited:
                    continue
                # 记录路径, 记录路径操作一定要在下一层迭代之前
                visited.add((x,y))
                #下一层决策
                backtrace(image, x, y)
                
               
        
        

        backtrace(image, sr, sc)
        return image

print(Solution().floodFill( [[0,0,1],[0,1,1]], 1, 1, 1))

                
            
