import sys


class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if x < 0:
            s_reverse = '-' + s[-1:0:-1]
        else:
            s_reverse = s[::-1]

        reverse_value = int(s_reverse)
        if (reverse_value >= (2 ** 31) - 1) or (reverse_value <= - (2 ** 31)):
            return 0

        return reverse_value


sol = Solution()
assert sol.reverse(-123) == -321, "ERROR: -123"
assert sol.reverse(-1534236469) == 0, "ERROR: -1534236469"
