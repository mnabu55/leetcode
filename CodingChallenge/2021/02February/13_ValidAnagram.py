'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_sort = sorted(s)
        t_sort = sorted(t)
        for char_s, char_t in zip(s_sort, t_sort):
            if char_s != char_t:
                return False
        return True

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c = Counter(s)
        print("c: ", c)
        return Counter(s) == Counter(t)


solution = Solution()
assert solution.isAnagram2("anagram", "nagaram") == True, "case01,ng"
