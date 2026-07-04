"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # BFS traversal
        # for each unvisited node, attach unvisited neighbors

        # thought: since there are no loops
        # does that mean you dont need to keep a visited set?

        # BFS traversal + hashing
        # old, and new copy
        # hashmap <oldNode, [new Node and neighbors it points to]>
        # the question is, how do you append nodes that dont exist yet?
        # well that must mean you need to create them first
        if not node:
            return None

        track = {}
        track[node] = Node(node.val)
        q = collections.deque([node])

        while q:
            oldNode = q.popleft()
            for n in oldNode.neighbors:
                if n not in track:
                    track[n] = Node(n.val)
                    q.append(n)
                track[oldNode].neighbors.append(track[n])

        return track[node]