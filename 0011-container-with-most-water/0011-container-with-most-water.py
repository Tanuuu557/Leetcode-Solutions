class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) -1
        max_water =0

        while left < right:
            width = right - left
            curr_water = min(height[left], height[right]) * width
            max_water = max(max_water, curr_water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
sol= Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
         