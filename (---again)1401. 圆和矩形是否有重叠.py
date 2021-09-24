class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x0, y0 = (x1 + x2) / 2, (y1 + y2) / 2
        c_x, c_y = abs(x_center - x0), abs(y_center - y0)
        v = (c_x - (x2 - x0), c_y - (y2 - y0))
        return max(v[0], 0)**2 + max(v[1], 0)**2 <= radius**2