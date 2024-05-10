'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
'''

def generateParens(n):
    stack = []
    res = []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append(''.join(stack))
            return
        
        if openN < n:
            stack.append('(')
            backtrack(openN + 1, closedN)
            # update stack, is a global variable
            stack.pop()

        if closedN < openN: # adds a closed parens
            stack.append(')')
            backtrack(openN, closedN + 1)
            stack.pop()

    backtrack(0, 0)
    return res

print(generateParens(3))