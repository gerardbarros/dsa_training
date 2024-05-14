'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''

def searchMatrix(matrix, target):
    rows = len(matrix) 
    cols = len(matrix[0])
    #look for row we need to find
    top = 0
    btm = rows - 1

    while top <= btm:
        row = (top + btm) // 2
        if target > matrix[row][-1]:
            # look for rows with larger values than current row
            top = row + 1
        elif target < matrix[row][0]:
            # target value is smaller than target value in row
            #look for rows with smaller values than current row
            botm = row - 1
        else:
            break

    if not (top <= btm): #none of the rows return target val
        return False
    # run bs on current row
    row = (top + btm) // 2
    l = 0
    r = cols - 1

    while l <= r:
        mid = (l + r) // 2
        if target > matrix[row][mid]:
            # search towards R of middle point
            l = mid + 1
        elif target < matrix[row][mid]:
            r = mid - 1
        else:
            return True
    return False
        #never found target val

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))