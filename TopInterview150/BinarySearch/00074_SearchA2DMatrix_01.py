from typing import List


class Solution:
    def searchMatrix_wa(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        left, right = 0, len(matrix[0]) - 1
        low, high = 0, len(matrix) - 1

        row, col = -1, -1
        while low <= high:
            row = low + (high - low) // 2
            if matrix[row][0] == target or matrix[row][right] == target:
                return True
            elif matrix[row][0] < target:
                low = row + 1
            else:
                high = row - 1

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix[0])-1
        low, high = 0, len(matrix)-1

        row, col = -1, -1
        while low <= high:
            row = low + (high - low) // 2
            if matrix[row][0] == target or matrix[row][right] == target:
                return True
            elif matrix[row][0] < target < matrix[row][right]:
                break
            elif target < matrix[row][0]:
                high = row - 1
            else:
                low = row + 1

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1

        return False


if __name__ == '__main__':
    solution = Solution()

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 3
    ans = True
    assert solution.searchMatrix(matrix, target) == ans

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 13
    ans = False
    assert solution.searchMatrix(matrix, target) == ans

    matrix = [[1], [3]]
    target = 3
    ans = True
    assert solution.searchMatrix(matrix, target) == ans

    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 11
    ans = True
    assert solution.searchMatrix(matrix, target) == ans
