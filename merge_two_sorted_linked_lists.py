'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]

Example 2:
Input: list1 = [], list2 = [1,2]
Output: [1,2]

Example 3:
Input: list1 = [], list2 = []
Output: []

Constraints:
0 <= The length of the each list <= 100.
-100 <= Node.val <= 100
'''

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    tail = dummy

    #if both lists are empty
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else: # list 1 and 2 are same
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    #find non empty list
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next