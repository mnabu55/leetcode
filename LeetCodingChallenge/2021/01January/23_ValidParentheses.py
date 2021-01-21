'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''


class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_opposite = {"}": "{", "]": "[", ")": "("}
        parentheses = "{[("
        stack = []
        for c in s:
            if c in parentheses:
                stack.append(c)
            elif c in parentheses_opposite:
                if len(stack) <= 0:
                    return False
                last = stack.pop()
                if last != parentheses_opposite[c]:
                    return False
        # print("stack: ", stack)
        return True if len(stack) == 0 else False


solution = Solution()
assert solution.isValid("()") == True, "case01,ng"
assert solution.isValid("()[]{}") == True, "case02,ng"
assert solution.isValid("(]") == False, "case03,ng"
assert solution.isValid("([)]") == False, "case04,ng"
assert solution.isValid("{[]}") == True, "case05,ng"
