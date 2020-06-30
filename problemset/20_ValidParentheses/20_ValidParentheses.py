'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        opening = set('([{')
        matches = set([('(', ')'), ('[', ']'), ('{', '}')])
        stack = []
        for paren in s:
            if paren in opening:
                stack.append(paren)
            else:
                if len(stack) == 0:
                    return False
                last_open = stack.pop()
                if (last_open, paren) not in matches:
                    return False

        return len(stack) == 0


ins = Solution()
# assert ins.isValid('[]') == True, "case 1 ng"
# assert ins.isValid('()[]{}') == True, "case 2 ng"
# assert ins.isValid('(]') == False, "case 3 ng"
# assert ins.isValid('([)]') == False, "case 4 ng"
# assert ins.isValid('{[]}') == True, "case 5 ng"
assert ins.isValid('((') == False, "case 6 ng"
