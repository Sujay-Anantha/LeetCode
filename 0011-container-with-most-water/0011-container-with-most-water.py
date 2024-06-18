class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        area = 0
        while left <= right:
            temp = (right - left) * min(height[left], height[right])
            area = max(area, temp)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1


        return area