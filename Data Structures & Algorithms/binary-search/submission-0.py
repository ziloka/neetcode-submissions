class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        return self.helper(nums, low, high, target)
    
    def helper(self, nums, low, high, target):
        if low > high:
            return -1
        
        middle = ((high - low) // 2) + low
        if nums[middle] == target:
            return middle

        if target < nums[middle]:
            return self.helper(nums, low, middle - 1, target)

        return self.helper(nums, middle + 1, high, target)