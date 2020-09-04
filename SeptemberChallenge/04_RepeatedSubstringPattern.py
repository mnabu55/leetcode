'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:
Input: "aba"
Output: False

Example 3:
\Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        len_s = len(s)

        for subst_len in range(1, len_s // 2 + 1):
            if len_s % subst_len != 0:
                continue
            else:
                # number_of_multiple = len_s // subst_len
                # subst = s[:subst_len]
                # if s == subst * number_of_multiple:
                if s == s[:subst_len] * (len_s // subst_len):
                    return True
        return False


solution = Solution()
assert solution.repeatedSubstringPattern("abab") == True, "case01,ng"
assert solution.repeatedSubstringPattern("aba") == False, "case02,ng"
assert solution.repeatedSubstringPattern("abcabcabcabc") == True, "case03,ng"
