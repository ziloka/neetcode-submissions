class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack: used to keep of problems that need to solved
        
        # you find max temperature
        # solve the previous subproblems now
        # since, you cannot get the difference in days via the temp val,
        # you must store the index in the stack
        result = [0] * len(temperatures)

        stack = collections.deque()
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                oldIndex = stack.pop()
                result[oldIndex] = i - oldIndex 
            stack.append(i)
        
        return result
            