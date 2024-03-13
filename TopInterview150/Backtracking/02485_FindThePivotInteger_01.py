

class Solution:
    def pivotInteger(self, n: int) -> int:
        left_sum = 0
        right_sum = n * (n + 1) // 2
        for pivot in range(1, n + 1):
            left_sum += pivot
            right_sum -= pivot - 1
            if left_sum == right_sum:
                return pivot

        return -1


if __name__ == '__main__':
    solution = Solution()
    assert solution.pivotInteger(n=8) == 6
    assert solution.pivotInteger(n=1) == 1
    assert solution.pivotInteger(n=4) == -1
