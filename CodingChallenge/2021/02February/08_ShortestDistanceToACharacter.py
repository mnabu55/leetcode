'''
Given a string s and a character c that occurs in s,
return an array of integers answer
where answer.length == s.length and
answer[i] is the shortest distance from s[i] to the character c in s.

Example 1:
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]

Example 2:
Input: s = "aaab", c = "b"
Output: [3,2,1,0]

Constraints:
1 <= s.length <= 104
s[i] and c are lowercase English letters.
c occurs at least once in s.
'''
from typing import List
import sys

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:

        # before = sys.maxsize
        before = -1
        result = [0 for _ in range(len(s))]
        stored = 0
        for current in range(len(s)):
            if s[current] == c:
                result[stored] = min(current - stored, before - stored)
                stored += 1
                before = current
            elif s[current] != c and before >= 0:
                result[stored] = min(current - stored, before - stored)

        print("result: ", result)
        return result


solution = Solution()
assert solution.shortestToChar("loveleetcode", "e") == [3,2,1,0,1,0,0,1,2,2,1,0], "case01,ng"
