class Solution:
    def climbStairs(self, n: int) -> int:
        # originally I thought that this was a combination problem, not a permutation problem
        # the order in which you climb the stairs also matter

        # to solve n = 1
        # 1
        # n = 2, sol(n=1) + 1
        # 1 + 1
        # 2
        # to solve n = 3, sol(n=2) + 1
        # 1 + 1 + 1
        # 2 + 1
        # 1 + 2
        # to solve n = 4, sol(n=3) = sol(2) + sol(1)
        # 1 + 1 + 1 + 1
        # 2 + 1 + 1
        # 1 + 1 + 2
        # 1 + 2 + 1
        # 2 + 2

        # it seems to build a staircase in a weird way.
        # lets describe this algorithm mechanically
        # add the last two steps together to get the next step

        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one
