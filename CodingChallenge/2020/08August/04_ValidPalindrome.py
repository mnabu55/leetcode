'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false

Constraints:
s consists only of printable ASCII characters.
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alphanumeric = "".join([c.lower() for c in s if c.isalnum()])
        for i in range(len(s_alphanumeric) // 2):
            if s_alphanumeric[i] != s_alphanumeric[- i - 1]:
                return False
        return True


solution = Solution()
assert solution.isPalindrome("A man, a plan, a canal: Panama") == True, "NG: case 1"
assert solution.isPalindrome("race a car") == False, "NG: case 2"
