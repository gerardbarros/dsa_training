'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
'''

# ITERATIVE SOLUTION
def reverseList(head):
    prev = None
    curr = head

    while curr:
        #temp var
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# RECURSIVE SOLUTION - needs extra memory
# def reverseList(head):
#     if not head:
#         return None
#     newHead = head
#     if head.next:
#         newHead = self.reverseList(head.next)
#         # reverse link from next node and head
#         head.next.next = head
#     head.next = None
#     return newHead

print(reverseList([1, 2, 3, 4, 5]))
print(reverseList([1, 2]))
print(reverseList([]))