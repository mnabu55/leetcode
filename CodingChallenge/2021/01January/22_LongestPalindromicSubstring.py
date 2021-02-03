'''
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        lps = ""
        n = len(s)
        for i in range(n):
            odd = self.expandPalindrome(s, i, i)
            even = self.expandPalindrome(s, i, i + 1)
            if len(lps) < len(odd):
                lps = odd
            if len(lps) < len(even):
                lps = even
        return lps

    def expandPalindrome(self, s: str, l: int, r: int) -> bool:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]


solution = Solution()
assert solution.longestPalindrome("babad") == "bab", "case01,ng"
assert solution.longestPalindrome("cbbd") == "bb", "case02,ng"
assert solution.longestPalindrome("ac") == "a", "case04,ng"
assert solution.longestPalindrome("bb") == "bb", "case05,ng"
assert solution.longestPalindrome("a") == "a", "case03,ng"
