class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # one pointer at the beginning, another at the end
        # you can compare the two pointers, 
        # also compare the one thats front/behind
        # move one of the pointers, depending on the difference to the target
        first = 0
        second = len(numbers) - 1
        while first != second:
            candidate = numbers[first] + numbers[second]
            if target == candidate:
                return [first+1, second+1]
            else:
                # if you're one off, you only need to move one pointer
                # if you're alot off, move both pointers

                # keep first there
                # move second until candidate < target, then move first
                if candidate < target:
                    first += 1
                else:
                    second -= 1

                # as soon as target is < candidate
                # if target < candidate:
                #     # first pointer moves lower
                #     first -= 1
                # elif target - candidate == 1:
                #     if numbers[first] - numbers[first+1] == 1:
                #         first += 1
                #     else:
                #         second -= 1
                # else:
                #     first += 1
                #     second -= 1
    