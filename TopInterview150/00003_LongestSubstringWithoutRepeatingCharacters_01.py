

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        left = 0
        longest = 0

        for right, char in enumerate(s):
            count[char] = count.get(char, 0) + 1
            while count[char] > 1:
                delete_char = s[left]
                count[delete_char] -= 1
                left += 1
            
            current_len = right - left + 1
            longest = max(longest, current_len)
        
        return longest


solution = Solution()
assert solution.lengthOfLongestSubstring(s = "abcabcbb") == 3
assert solution.lengthOfLongestSubstring(s = "bbbbb") == 1
assert solution.lengthOfLongestSubstring(s = "pwwkew") == 3