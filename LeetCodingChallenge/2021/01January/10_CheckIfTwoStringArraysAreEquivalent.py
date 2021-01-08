'''
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

Example 2:
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

Example 3:
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true

Constraints:
1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.
'''

from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # concatenate all word into one string both word1 and word2
        word1_string = "".join([x1 for x1 in word1])
        word2_string = "".join([x2 for x2 in word2])

        # check word1's string and word2's string are same
        if len(word1_string) != len(word2_string):
            return False
        for i in range(len(word1_string)):
            if word1_string[i] != word2_string[i]:
                return False
        return True


solution = Solution()
assert solution.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]) == True, "case01,ng"
assert solution.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]) == False, "case02,ng"

