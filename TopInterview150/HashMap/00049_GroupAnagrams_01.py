from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if not sorted_word in seen:
                seen[sorted_word] = [word]
            else:
                seen[sorted_word].append(word)

        anagram_groups = []
        for words in seen.values():
            anagram_groups.append(words)
        
        return anagram_groups


solution = Solution()
assert solution.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]]