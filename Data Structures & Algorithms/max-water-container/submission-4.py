class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # amount of water formula
        # min bar (height) * distance between bars (width)
        
        # brute force solution O(n^2)
        # test every two bar combination, and return
        # max amount of amount of water
        # in the container

        # optimized solution O(n)
        # two pointers
        # shift the shortest bar every time
        # and test the bars
        maxWater = 0

        l = 0
        r = len(heights) - 1
        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            maxWater = max(maxWater, height*width)

            # move shorter bar
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxWater