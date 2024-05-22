'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find midpoint
        slow = head
        fast = head.next
        #fast not nujll and nost end of list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        #reverse second half of list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #merge the two halves of list
        first = head
        second = prev
        #keep going til one pointer is null
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1 #bc were insertintg second node between first and first.next
            #shift pointers
            first = temp1
            second = temp2