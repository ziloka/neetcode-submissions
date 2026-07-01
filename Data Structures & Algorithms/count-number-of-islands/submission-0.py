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
        visited = set()
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if (r, c) in visited:
                    continue
                
                if grid[r][c] == "1":
                    numIslands += 1

                    # attempt to visit the entire island via DFS
                    q = collections.deque()
                    q.append((r, c))
                    while q:
                        er, ec = q.pop()

                        if (er, ec) not in visited:
                            # land that was linked to the original land
                            # is marked as visited. So that new iterations
                            # do not attempt to reiterate through the same island
                            visited.add((er, ec))

                        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                            if 0 <= er + dr < NUM_ROWS and \
                               0 <= ec + dc < NUM_COLS and \
                               grid[er + dr][ec + dc] == "1":
                               # do not visit the same piece of land twice
                               grid[er + dr][ec + dc] = "0"
                               q.append((er + dr, ec + dc))
        return numIslands
                