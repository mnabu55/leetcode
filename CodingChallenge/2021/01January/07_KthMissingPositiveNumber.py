'''
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

Constraints:
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
'''

from typing import List


class Solution:

    # max value of list
    max_value = 10000

    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_count = 0
        arr_index = 0
        len_arr = len(arr)
        for n in range(1, self.max_value + 1):
            if arr_index < len_arr:
                if n == arr[arr_index]:
                    arr_index += 1
                else:
                    missing_count += 1
                    if missing_count >= k:
                        return n
            else:
                return n + (k - 1 - missing_count)


solution = Solution()
assert solution.findKthPositive([2,3,4,7,11], 5) == 9, "case01,ng"
assert solution.findKthPositive([1,2,3,4], 2) == 6, "case02,ng"
