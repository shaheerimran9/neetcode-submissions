# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseList(head):
            prev, curr = None, head
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        
        #Find Middle of LinkedList
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Reverse Second Half of LinkedList
        secondHalf = reverseList(slow.next)
        slow.next = None

        #Reverse Pointers
        first, second = head, secondHalf
        while first and second:
            tempFirst, tempSecond = first.next, second.next
            first.next = second
            second.next = tempFirst
            first, second = tempFirst, tempSecond

        