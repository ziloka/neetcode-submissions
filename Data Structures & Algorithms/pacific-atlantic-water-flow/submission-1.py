class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.NUM_ROWS = len(heights)
        self.NUM_COLS = len(heights[0])

        result = []
        for r in range(self.NUM_ROWS):
            for c in range(self.NUM_COLS):
                if self.flowBothOceans(heights, r, c):
                    result.append([r, c])
        return result

    def flowBothOceans(self, heights, r, c):
        hitPacific = False
        hitAtlantic = False

        q = collections.deque([(r, c)])
        visited = set()
        while q and not (hitPacific and hitAtlantic):
            r, c = q.pop()

            # check if Pacific or Atlantic, via check if element is on the edge
            if r == 0 or c == 0:
                hitPacific = True
            # can't use elif, bc corners are true for both
            # automatically
            if r == self.NUM_ROWS - 1 or c == self.NUM_COLS - 1:
                hitAtlantic = True

            visited.add((r, c))

            # append new visitors, no visitors? not EXIT
            # no visitors mean that split of the water has no where else it can visit
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                vr = r + dr
                vc = c + dc
                if 0 <= vr < self.NUM_ROWS and \
                   0 <= vc < self.NUM_COLS and \
                   (vr, vc) not in visited and \
                   heights[vr][vc] <= heights[r][c]:
                    q.append((r + dr, c + dc))
        return hitPacific and hitAtlantic
