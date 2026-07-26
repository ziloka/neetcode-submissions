class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # pattern?
        # BFS, since rotten fruit spreads to what is closest
        # invariant pattern holds?
        # a fresh fruit cell can only be declared rotten
        # when a rotten fruit is near it
        # enumerated states
        # FRESH: fresh fruit
        # ROTTEN: rotten fruit
        # data structure mapping?
        # use visited set, to track rotten fruit locations
        # declarative transitions?
        # ROTTEN FRUIT + fresh fruit nearby -> becomes rotten
        # ROTTEN FRUIT + no fruit nearby -> particular path is done
        # ROTTEN FRUIT + all rotten fruit -> done, no need to repeat
        
        # imperatively
        # start at all rotten fruits, run BFS on each of them
        # stop when there are no more new fresh fruit
        # to cover in that area

        # weird that question said "minimum number of minutes"
        
        fresh_fruit = 0
        queue = collections.deque()
        # get the possible starting points
        # run one step for each rotten fruit
        # increment minute, and repeat
        NUM_ROWS = len(grid)
        NUM_COLS = len(grid[0])
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if grid[r][c] == 1:
                    fresh_fruit += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        # now since we have starting points we
        # iterate through each of them, 
        # pop them, and append the new elements
        minutes = 0
        while queue:
            LEN = len(queue)
            for _ in range(LEN):
                row, col = queue.popleft()
                
                # if theres fresh fruit nearby the currently rotten one, spread to it
                for row, col in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                    if 0 <= row < NUM_ROWS and 0 <= col < NUM_COLS and grid[row][col] == 1:
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh_fruit -= 1

            # more fresh fruit to spread to, continue counting
            if len(queue) != 0:
                minutes += 1

        return minutes if fresh_fruit == 0 else -1