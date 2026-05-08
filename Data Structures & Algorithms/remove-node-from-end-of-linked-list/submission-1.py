# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create distance between 2 pointers first and then increment the fast pointer to the end
        dummy = ListNode(0, head)
        slow = dummy # we increment one before the head so the spacing is right
        fast = head
        for _ in range(n):
            fast = fast.next


        while fast is not None:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next

        return dummy.next # the head
