'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.


Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1

Constraints:
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100

'''

def diamOfBinTree(root):
    res = [0]

    def dfs(root):
        if not root:
            return -1 #heigh of null tree is -1
        left = dfs(root.left) #height of left
        right = dfs(root.right) #height of right

        #find diameter of current root we're traversing by finding height of L and R
        res[0] = max(res[0], 2 + left + right)

        # return height runnign through root node
        return 1 + max(left, right)
    
    dfs(root)
    return res[0]