'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict = {}

        def _wordBreak(s: str, wordDict: List[str], wordtable: dict) -> bool:
            if s in wordDict:
                return True
            if s in wordtable:
                return wordtable[s]
            for i in range(1, len(s) + 1):
                left = s[0:i]
                if left in wordDict and _wordBreak(s[i:], wordDict, wordtable):
                    print("left: {}, found".format(left))
                    print("call self.wordBreak: ", s[i:])
                    wordtable[s] = True
                    return True
            wordtable[s] = False
            return False

        return _wordBreak(s, wordDict, dict)


solution = Solution()
assert solution.wordBreak("leetcode", ["leet", "code"]) == True, "case01,ng"
assert solution.wordBreak("applepenapple", ["apple", "pen"]) == True, "case02,ng"
assert solution.wordBreak("catsandog", ["cats","dog","sand","and","cat"]) == False, "case03,ng"

