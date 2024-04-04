from typing import List


class Solution:
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        word_table = {}

        def helper(s: str, wordDict: List[str], wordTable: dict) -> bool:
            if s in wordDict:
                return True
            if s in wordTable:
                return wordTable[s]
            
            n = len(s)
            for i in range(1, n + 1):
                left = s[0:i]
                if left in wordDict and helper(s[i:], wordDict, wordTable):
                    wordTable[s] = True
                    return True

            wordTable[s] = False
            return False

        return helper(s, wordDict, word_table)


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def construct(current,wordDict, memo={}):
            if current in memo:
                return memo[current]

            if not current:
                return True

            for word in wordDict:
                if current.startswith(word):
                    new_current = current[len(word):]
                    if construct(new_current,wordDict,memo):
                        memo[current] = True
                        return True

            memo[current] = False
            return False

        return construct(s,wordDict)


if __name__ =="__main__":
    solution = Solution()

    s = "leetcode"
    wordDict = ["leet","code"]
    expected = True
    assert solution.wordBreak(s, wordDict) == expected

    s = "applepenapple"
    wordDict = ["apple","pen"]
    expected = True
    assert solution.wordBreak(s, wordDict) == expected

    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    expected = False
    assert solution.wordBreak(s, wordDict) == expected
