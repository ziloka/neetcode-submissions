class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # naive solution O(n) space complexity
        # use a set, check if element in set
        # store each element in set
        # check if element in set
        # true, return element
        # otherwise continue loop

        # optimized solution O(1) space complexity
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                return abs(nums[i])
            else:
                nums[abs(nums[i]) - 1] *= -1
        return 0