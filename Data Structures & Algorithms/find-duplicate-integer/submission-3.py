class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # naive solution O(n) space complexity
        # use a set, check if element in set
        # store each element in set
        # check if element in set
        # true, return element
        # otherwise continue loop

        # two pointers: slow, and fast pointer
        # good for cycles in LL, and duplicates
        # slow pointer will only iterate over len(nums) / 2 elements
        # while fast pointer iterates over every other char
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow
    
        # slow = 0
        # fast = 1
        # while fast < len(nums):
        #     if nums[slow] == nums[fast]:
        #         return nums[slow]

        #     slow += 1
        #     fast += 2
        # # if len(nums) <= 1, no duplicates
        # return -1