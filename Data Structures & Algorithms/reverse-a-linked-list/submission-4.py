# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            #Save next node link
            next_node = curr.next
            #Reverse pointers
            curr.next = prev
            #Move pointers up
            prev = curr
            curr = next_node
        return prev