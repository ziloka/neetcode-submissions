# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 0, 1, 2, 3
# 1, 0, 2, 3
# 2, 1, 0, 3
# 3, 2, 1, 0

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        tail = head;
        while head.next != None:
            second = head.next
            head.next = second.next
            second.next = tail
            tail = second
        return tail;