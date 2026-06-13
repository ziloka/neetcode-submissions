"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # reason through this step by step
        # well, to make a copy of a singly linked list
        # you would instantiate a new node with the appropriate
        # value for each iteration of the linked list

        # what about linked lists with random pointers?
        # you can copy the reference of the random pointer
        # easily, but it would break the note in the problem
        # this must mean that you somehow need to use the value
        # of the node, and the position of the node that it points to,
        # to solve the problem.

        # naive algorithm. O(n^2)
        # copy LL as if singly linked list
        # for each random member in node in the linked list, 
        # and each node in the linked list
        # count nth position, and find the node that points to same reference
        # assign that node to be the random member and move to next node
        # return the head

        # optimized time complexity guess O(n), space complexity O(n)
        # cannot use recursion, cannot break problem into subproblems
        # throw in a hashmap? <(position, val), node reference>
        # copy singly LL, copying position, val, and node to map
        # OH IM STUPID: map<old node, new node>, to assign random pointer
        # hashmaps and arrays dont work
        # two pointers dont work
        # thought: this seems like a cycle, so two pointers might be possible
       
        # invariants: empty LL, one LL, many LL
        if not head:
            return None

        # The cache map will map: Old Node -> New Node
        # We can explicitly map None to None to handle empty next/random pointers gracefully
        cache = {None: None}

        curr = head
        while curr:
            cache[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            new_node = cache[curr]
            new_node.next = cache[curr.next]
            new_node.random = cache[curr.random]
            curr = curr.next

        return cache[head]