'''

'''

from typing import List

class Solution:

    # def __init__(self):
    #     self.mat = []

    def numSpecial(self, mat: List[List[int]]) -> int:
        # self.mat = mat
        rows = len(mat)
        cols = len(mat[0])
        number_of_special_positions = 0
        count_one_each_rows_cols = []

        for i in range(rows):
            count_one_each_rows_cols.append([0 for _ in range(cols)])
        print(count_one_each_rows_cols)

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
