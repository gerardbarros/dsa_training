'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.


Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]


Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?
'''

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    l = dummy
    r = head
    #once n is 0 we shifted by the amount we wanted to shfit by
    while n > 0 and r:
        r = r.next
        n -= 1
    #shift l and r until r reaches end of list
    while r:
        l = l.next
        r = r.next

    # delete node
    l.next = l.next.next
    return dummy.next # dont include the dummy node in the output
