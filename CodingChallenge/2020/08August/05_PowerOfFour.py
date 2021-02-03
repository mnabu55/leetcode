'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion_I?
'''


import math

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 0:
            return False
        return (num != 0 and ((num & (num - 1)) == 0) and not (num & 0xAAAAAAAA));


solution = Solution()
assert solution.isPowerOfFour(16) == True, "case 1 NG"
assert solution.isPowerOfFour(5) == False, "case 2 NG"
