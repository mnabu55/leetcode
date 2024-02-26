from typing import List
import sys


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, window_sum = 0, 0
        min_len = sys.maxsize
        
        for right, num in enumerate(nums):
            window_sum += num

            while window_sum >= target:
                current_len = right - left + 1
                min_len = min(min_len, current_len)

                window_sum -= nums[left]
                left += 1

        return min_len if min_len != sys.maxsize else 0


    def minSubArrayLen_wa(self, target: int, nums: List[int]) -> int:
        min_size = sys.maxsize
        current_sum = 0
        start = end = 0
        n = len(nums)
        
        while end < n:
            current_sum += nums[end]
            end += 1
            if current_sum < target:
                continue

            min_size = min(min_size, end - start + 1)

            while start <= end and current_sum >= target:
                current_sum -= nums[start]
                start += 1
                if current_sum > target:
                    min_size = min(min_size, end - start + 1)
        
        print(min_size)
        return min_size


solution = Solution()
assert solution.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]) == 2

