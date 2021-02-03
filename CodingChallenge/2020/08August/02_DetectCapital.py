'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

1) All letters in this word are capitals, like "USA".
2) All letters in this word are not capitals, like "leetcode".
3) Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:
Input: "USA"
Output: True

Example 2:
Input: "FlaG"
Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
'''


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        result = False

        # check case 1
        upper = word.upper()
        if word == upper:
            result = True

        # check case 2
        lower = word.lower()
        if word == lower:
            result = True

        # check case 3
        capitalized = word.capitalize()
        if word == capitalized:
            result = True

        return result


solution = Solution()
assert solution.detectCapitalUse("USA") == True, "case 1 NG"
assert solution.detectCapitalUse("FlaG") == False, "case 2 NG"
