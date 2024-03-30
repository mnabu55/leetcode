


class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            mid = low + (high - low) // 2
            square_mid = mid * mid
            if square_mid == x:
                return mid
            elif square_mid < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return high


if __name__ == '__main__':
    solution = Solution()

    x = 4
    expected = 2
    assert solution.mySqrt(x) == expected

    x = 8
    expected = 2
    assert solution.mySqrt(x) == expected

    x = 1
    expected = 1
    assert solution.mySqrt(x) == expected

    x = 6
    expected = 2
    assert solution.mySqrt(x) == expected
