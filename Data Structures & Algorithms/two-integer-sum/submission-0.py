class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in table:
                return [table[complement], i]
            else:
                table[n] = i;
        return []
                