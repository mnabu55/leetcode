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
    check_func = ["is_upper", "is_lower", "is_capitalize"]

    def is_upper(self, word):
        s = word.upper()
        return word == s

    def is_lower(self, word):
        s = word.lower()
        return word == s

    def is_capitalize(self, word):
        s = word.capitalize()
        return word == s

    def detectCapitalUse(self, word: str) -> bool:
        result = False

        for func in self.check_func:
            func_symbol = "self.{}(word)".format(func)
            if eval(func_symbol):
                result = True

        return result


solution = Solution()
assert solution.detectCapitalUse("USA") == True, "case 1 NG"
assert solution.detectCapitalUse("FlaG") == False, "case 2 NG"
assert solution.detectCapitalUse("leetcode") == True, "case 3 NG"

