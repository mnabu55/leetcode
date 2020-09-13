'''
Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.
A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

Example 1:
Input: mat = [[1,0,0],
              [0,0,1],
              [1,0,0]]
Output: 1
Explanation: (1,2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

Example 2:
Input: mat = [[1,0,0],
              [0,1,0],
              [0,0,1]]
Output: 3
Explanation: (0,0), (1,1) and (2,2) are special positions.

Example 3:
Input: mat = [[0,0,0,1],
              [1,0,0,0],
              [0,1,1,0],
              [0,0,0,0]]
Output: 2

Example 4:
Input: mat = [[0,0,0,0,0],
              [1,0,0,0,0],
              [0,1,0,0,0],
              [0,0,1,0,0],
              [0,0,0,1,1]]
Output: 3

Constraints:
rows == mat.length
cols == mat[i].length
1 <= rows, cols <= 100
mat[i][j] is 0 or 1.
'''

from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        number_of_special_positions = 0
        count_one_each_rows_cols = []

        for i in range(rows):
            count_one_each_rows_cols.append([0 for _ in range(cols)])

        for r in range(rows):
            for c in range(cols):
                for rows_idx in range(rows):
                    count_one_each_rows_cols[r][c] += mat[rows_idx][c]
                for cols_idx in range(cols):
                    count_one_each_rows_cols[r][c] += mat[r][cols_idx]

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1 and count_one_each_rows_cols[r][c] == 2:
                    number_of_special_positions += 1

        return number_of_special_positions


solution = Solution()
assert solution.numSpecial([[1,0,0],[0,0,1],[1,0,0]]) == 1, "case01, ng"
assert solution.numSpecial([[1,0,0],[0,1,0],[0,0,1]]) == 3, "case02, ng"
assert solution.numSpecial([[0,0],[0,0],[1,0]]) == 1, "case03, ng"
