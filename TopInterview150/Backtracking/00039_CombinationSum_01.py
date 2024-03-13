from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtrack(combination, current_sum, start):
            if current_sum == target:
                combinations.append(combination.copy())
                return
            elif current_sum > target:
                return
            
            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(combination, current_sum + candidates[i], i)
                combination.pop()

        backtrack([], 0, 0)
        return combinations


if __name__ == "__main__":
    s = Solution()

    candidates = [2, 3, 6, 7]
    target = 7
    result = [[2, 2, 3], [7]]
    assert s.combinationSum(candidates, target) == result
