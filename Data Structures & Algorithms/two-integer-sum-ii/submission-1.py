class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # one pointer at the beginning, another at the end
        # you can compare the two pointers, 
        # also compare the one thats front/behind
        # move one of the pointers, depending on the difference to the target
        first = 0
        second = len(numbers) - 1
        while first < second:
            candidate = numbers[first] + numbers[second]
            if target == candidate:
                return [first+1, second+1]
            elif candidate < target:
                first += 1
            else:
                second -= 1


    