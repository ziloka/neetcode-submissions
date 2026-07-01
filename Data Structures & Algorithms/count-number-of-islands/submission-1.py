class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS (post traversal?)
        # iterate through each element in matrix
        # hit new land, increment answer
        # and visit the entire island 
        # rise and repeat

        numIslands = 0

        NUM_ROWS = len(grid)
        NUM_COLS = len(grid[0])
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):               
                if grid[r][c] == "1":
                    numIslands += 1

                    # attempt to visit the entire island via DFS
                    grid[r][c] = "0"
                    stack = [(r, c)]
                    while stack:
                        er, ec = stack.pop()

                        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                            nr, nc = er + dr, ec + dc
                            if 0 <= nr < NUM_ROWS and \
                               0 <= nc < NUM_COLS and \
                               grid[nr][nc] == "1":
                               # do not visit the same piece of land twice
                               grid[nr][nc] = "0"
                               stack.append((nr, nc))
        return numIslands
                