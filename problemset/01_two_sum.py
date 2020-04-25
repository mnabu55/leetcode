from functools import reduce

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        len_nums = len(nums)
        is_found = False
        for i in range(0, len_nums - 1):
            for j in range(i + 1, len_nums):
                if nums[i] + nums[j] == target:
                    is_found = True
                    break
            else:
                continue
            break

        if not is_found:
            return []
        return [i, j]

sol = Solution()
assert sol.twoSum([1,2], 3) == [0, 1], "ERROR: [1, 2], 3"
