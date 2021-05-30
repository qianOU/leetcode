class Solution:
    def maximumTime(self, time: str) -> str:
        area = list(time)
        for idx, i in enumerate(time):
            if i=='?':
                if idx == 0: area[idx] = '2' if area[1] not in '456789' else '1'
                elif idx == 1: area[idx] = '3' if area[0] == '2' else '9'
                elif  idx == 3: area[idx] = '5'
                else: area[idx] = '9'
        
        return ''.join(area)