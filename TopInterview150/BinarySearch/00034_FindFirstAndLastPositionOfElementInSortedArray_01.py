from typing import List


class Solution:
    def searchRange_1(self, nums: List[int], target: int) -> List[int]:

        def binary_search_first(nums, target) -> int:
            low, high = 0, len(nums) - 1

            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    if mid - 1 >= 0 and nums[mid - 1] == target:
                        high = mid - 1
                    else:
                        return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return -1

        def binary_search_last(nums, target) -> int:
            low, high = 0, len(nums) - 1

            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    if mid + 1 < len(nums) and nums[mid + 1] == target:
                        low = mid + 1
                    else:
                        return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return -1

        start = binary_search_first(nums, target)
        end = binary_search_last(nums, target)

        return [start, end]


if __name__ == "__main__":
    solution = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(solution.searchRange(nums, target))
