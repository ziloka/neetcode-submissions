class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force solution O(n)
        # product of all nums
        # for i in length of nums
        # output at i is the product / nums of i

        # We can use the prefix and suffix technique.
        # First, we iterate from left to right and store the prefix products for each index in a prefix array,
        # excluding the current index's number.
        # Then, we iterate from right to left and store the suffix products for each index in a suffix array,
        #  also excluding the current index's number. Can you figure out the solution from here? 

        # three pass O(n) solution w/o division
        # aggregate, prefix numbers
        # aggregate suffix numbers
        # do multiplication to build final output

        prefix = [1] * len(nums)
        temp = 1 # keep track of running count
        for i in range(1, len(nums)):
            temp *= nums[i-1]
            prefix[i] = temp

        suffix = [1] * len(nums)
        temp = 1
        for i in range(len(nums)-2, -1, -1): # [len, 1)
            temp *= nums[i+1]
            suffix[i] = temp
        
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        return res