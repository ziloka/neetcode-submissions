class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force approach O(n^2)
        # find index of tallest and second tallest bars
        # calculate amount of water container stores
        # amount of water, height * width

        # two pointers, one of the left, and right
        # move shorter bar in the attempt to increase height
        # width would always be shorter
        res = 0
        
        left, right = 0, len(heights)-1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            res = max(res, width*height)

            # what bar is shorter?
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res