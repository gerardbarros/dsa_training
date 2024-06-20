'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''

def maxDepth(root):
    stack = [[root, 1]]
    res = 0 # if starts at 0 so if there is null rootnode, loop will execute but if wont start and rs stays 0
    
    while stack: #stack not empty
        node, depth = stack.pop() #pop 2 vals

        if node: # node not null
            res = max(res, depth)
            stack.append([node.left, depth + 1]) # add children of the node and the depth of each one ignore if null
            stack.append([node.right, depth + 1]) # add children of the node and the depth of each one ignore if null
    return res