'''
Given a string S, we can transform every letter individually
to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create.
You can return the output in any order.

Example 1:
Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:
Input: S = "3z4"
Output: ["3z4","3Z4"]

Example 3:
Input: S = "12345"
Output: ["12345"]

Example 4:
Input: S = "0"
Output: ["0"]

Constraints:
S will be a string with length between 1 and 12.
S will consist only of letters or digits.
'''
from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = []

        def helper(S, i, result):
            if i >= len(S) - 1:
                if S[i].isalpha():
                    return [S[i].lower(), S[i].upper()]
                else:
                    return [S[i]]
            len_S = len(S)
            start = i
            while i < len_S and not S[i].isalpha():
                i += 1
            if i >= len_S:
                return [S]
            end = i
            # tmp_result = helper(S, i + 1, result)
            tmp_result = helper(S, i+1, result)
            new_result = []
            for sub in tmp_result:
                new_result.append(S[start:end].lower() + sub)
                new_result.append(S[start:end].upper() + sub)
            return new_result

        result = helper(S, 0, result)
        print("result: ", result)
        return result


solution = Solution()
assert solution.letterCasePermutation("a1b2") == ["a1b2","a1B2","A1b2","A1B2"], "case01,ng"
assert solution.letterCasePermutation("12345") == ["12345"], "case02,ng"
assert solution.letterCasePermutation("37c") == ["37c", "37C"], "case03,ng"
