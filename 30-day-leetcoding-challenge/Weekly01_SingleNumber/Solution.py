from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        for item in nums:
            if item in dict:
                dict[item] += 1
            else:
                dict[item] = 1

        target = 0
        for item in dict:
            if dict[item] == 1:
                target = int(item)
                break

        return target


sol = Solution()
assert sol.singleNumber([2, 2, 1]) == 1, "ERROR! case [2,2,1]"
assert sol.singleNumber([4, 1, 2, 1, 2]) == 4, "ERROR! case [4,1,2,1,2]"
