

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        elif n == 0 or x == 1:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1 / x

        if n % 2 == 0:
            return self.myPow(x, n // 2) ** 2
        else:
            return self.myPow(x, n // 2) * self.myPow(x, (n // 2) + 1)


if __name__ == '__main__':
    solution = Solution()

    x = 2.00000
    n = 10
    expected = 1024.00000
    assert solution.myPow(x, n) == expected
