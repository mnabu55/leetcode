'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        reverse = s[::-1]
        for i in range(len(s)):
            if s[i] != reverse[i]:
                return False
        return True

    def isPalindrome2(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    def isPalindrome3(self, x: int) -> bool:
        return False if x < 0 else x == int(str(x)[::-1])


solution = Solution()
assert solution.isPalindrome3(-121) == False, "case 1 ng"
assert solution.isPalindrome3(10) == False, "case 2 ng"
assert solution.isPalindrome3(121) == True, "case 3 ng"
