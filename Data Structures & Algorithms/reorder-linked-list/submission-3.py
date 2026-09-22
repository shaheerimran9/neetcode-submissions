# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Split the LL
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l1 = head
        l2 = slow.next
        slow.next = None

        #Reverse Second List
        prev = None
        curr = l2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        l2 = prev

        #Modify Pointers
        while l1 and l2:
            temp_1 = l1.next
            temp_2 = l2.next

            l1.next = l2
            l2.next = temp_1
            
            l1 = temp_1
            l2 = temp_2
