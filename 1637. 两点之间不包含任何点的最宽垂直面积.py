class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = sorted(points, key=lambda x: x[0])
        m_width = 0
        for i in range(len(arr)-1):
            m_width = max(m_width, arr[i+1][0] - arr[i][0])
        return m_width
