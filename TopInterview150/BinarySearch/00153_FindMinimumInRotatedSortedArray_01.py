from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # if mid_value > right_value, part [mid, right] of array is pivotted.
            # so minimum value must be existed after (mid + 1) position
            if nums[mid] > nums[right]:
                left = mid + 1

            # if mid_value < right_value, part [mid, right] of array is sorted.
            # so minimum value must be existed equal than smaller than mid
            elif nums[mid] < nums[right]:
                right = mid

        return nums[left]        



if __name__ == '__main__':
    solution = Solution()

    nums = [3,4,5,1,2]
    expected = 1
    solution.findMin(nums) == expected

    nums = [4,5,6,7,0,1,2]
    expected = 0
    solution.findMin(nums) == expected

    nums = [11,13,15,17]
    expected = 11
    solution.findMin(nums) == expected
