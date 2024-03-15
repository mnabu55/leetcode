from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total_water = 0
        max_left, max_right = 0, 0
        left, right = 0, n-1
        while left < right:
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    total_water += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    total_water += max_right - height[right]
                right -= 1

        return total_water


if __name__ == "__main__":
    solution = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(solution.trap(height))
