class Solution:
    def removeSubfolders(self, folder):
        folder.sort(key=lambda x: x.count('/'))
        print(folder)
        path = set()
        ans = []
        for i in folder:
            tmp = i.split('/')
            for j in range(2, len(tmp)+1):
                sufix =  '/'.join(tmp[:j])
                if sufix in path:
                    break
            else:
                path.add(i)
                ans.append(i)
        
        return ans

print(Solution().removeSubfolders(
["/a","/a/b","/c/d","/c/d/e","/c/f"]))