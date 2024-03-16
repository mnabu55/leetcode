import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True


if __name__ == '__main__':
    solution = Solution()

    s = "A man, a plan, a canal: Panama"
    expected = True
    assert solution.isPalindrome(s) == expected

    s = "race a car"
    expected = False
    assert solution.isPalindrome(s) == expected

    s = " "
    expected = True
    assert solution.isPalindrome(s) == expected
