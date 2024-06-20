'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false


Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104

'''

def sameTree(p, q):
    if not p and not q: #emtpy trees
        return True
    if not p or not q or p.val != q.val: #only one is null
        return False
    # the two return vals, if and is true is true, if false, return false
    return (self.sameTree(p.left, q.left) and 
            self.sameTree(p.right, q.right))