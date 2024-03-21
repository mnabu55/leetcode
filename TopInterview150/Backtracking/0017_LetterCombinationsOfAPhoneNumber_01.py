from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(ans, digits, combination, index):
            if len(digits) < index:
                return
            
            if len(combination) == len(digits):
                ans.append(combination)
                return
            
            currentDigit = digits[index]
            currentString = map[currentDigit]

            for i in range(len(currentString)):
                backtrack(ans, digits, combination + currentString[i], index + 1)

        if len(digits) <= 0:
            return []
        
        ans = []
        backtrack(ans, digits, "", 0)
        
        return ans


if __name__ =="__main__":
    solution = Solution()

    digits = "23"
    expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert solution.letterCombinations(digits) == expected

    digits = ""
    expected = []
    assert solution.letterCombinations(digits) == expected

    digits = "2"
    expected = ["a", "b", "c"]
    assert solution.letterCombinations(digits) == expected
