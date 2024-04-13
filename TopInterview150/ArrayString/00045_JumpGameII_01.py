from typing import List


class Solution:
    def jump_wa(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf') for _ in range(n)]
        dp[0] = 0
        max_jump_len = nums[0]

        for i in range(1, n):
            last_index = max(0, i - max_jump_len)
            if last_index + nums[last_index] >= n - 1:
                return dp[last_index] + 1
            dp[i] = min(dp[i], dp[last_index] + 1)
            max_jump_len = max(max_jump_len, nums[i])
        
        return dp[n-1]


    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        destination = n - 1
        furthest = 0
        end = 0
        ans = 0

        for i in range(n - 1):
            furthest = max(furthest, i + nums[i])
            if furthest >= destination:
                return ans + 1

            if i == end:
                ans += 1
                end = furthest

        return ans


    def jump_2(self, nums: List[int]) -> int:
        n = len(nums)
        destination = n - 1         # destination is last index
        cur_coverage, last_index = 0, 0    # record of current coverage, record of last jump index
        count = 0              # counter for jump
        
        # Quick response if start index == destination index == 0
        if n == 1:
            return 0
        
        for i in range(n):
            # extend current coverage as further as possible
            cur_coverage = max(cur_coverage, i + nums[i])

            # forced to jump (by lazy jump) to extend coverage  
            if i == last_index:
                # update last jump index
                last_index = cur_coverage
                
                # update counter of jump by +1
                count += 1
                
                # check if reached destination already
                if cur_coverage >= destination:
                    return count
                
        return count

if __name__ == '__main__':
    solution = Solution()

    nums = [2,3,1,1,4]
    expected = 2
    assert solution.jump(nums) == expected

    nums = [2,3,0,1,4]
    expected = 2
    assert solution.jump(nums) == expected

    nums = [1,2,0,1]
    expected = 2
    assert solution.jump(nums) == expected

    nums = [1,2]
    expected = 1
    assert solution.jump(nums) == expected

    nums = [1,2,1,1,1,1]
    expected = 4
    assert solution.jump(nums) == expected
